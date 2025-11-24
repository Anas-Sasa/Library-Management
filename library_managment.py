"""
library_management_v1.py

Command-line Books Library manager:

This script provides a simple CSV-backed library system with two files:
- library.csv for available books
- checked-out.csv for borrowed books

Features:
- create CSV files with headers if missing
- add a book with input validation (ISBN, title, author)
- check out a book (move row from library.csv to checked-out.csv)
- check in a book (move row from checked-out.csv back to library.csv)
- remove rows by ISBN, display CSV content using pandas
- simple CLI menu for user interaction

Intended audience: beginners learning Python, file I/O, pandas and basic CLI UX.
"""

# [ BOOKS LIBRARY ] --> Editing on [ 23 Nov 2025 ]


# Import pandas for CSV reading/writing convenience, os for filesystem ops, time for delays
import pandas,os, time

# Import csv.writer for appending rows to CSV files
from csv import writer


# Build an absolute path for the main library CSV file in the current working directory
library = os.path.join(os.getcwd(), "library.csv") 

# Build an absolute path for the checked-out CSV file in the current working directory
checked_out_books = os.path.join(os.getcwd(), "checked-out.csv")


def clear_terminal():

    # Clear the terminal screen depending on operating system: Windows uses 'cls', POSIX uses 'clear'
    os.system("cls" if os.name == "nt" else "clear")


def sleep(second):
    # Pause execution for the given number of seconds (simple wrapper)
    time.sleep(second)


# Ensure a CSV file exists and contains the header row if it was missing or empty
def generate_file(file_name):
    # If the file does not exist or the file is empty, create it and write a header
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:

        with open(file_name, "w", newline="") as f:

            writer(f).writerow( ["isbn", "author", "book_title"] ) 

# Check whether a given ISBN already exists in the given CSV file
def is_isbn_exist(new_isbn,filename):

    # Read the CSV file into a pandas Series of isbn values with all columns as strings
    filename = pandas.read_csv(filename, dtype= str)["isbn"]

    # Check each existing ISBN for equality with the new one
    for exist_isbn in filename:

        if new_isbn == exist_isbn: 

            return True
            
    else:
        # If loop completes with no match return False
        return False

# Append a new row to the library CSV with the provided isbn, author and title
def store_data(new_isbn, author_name, book_title):


    with open(library, "a", newline= "") as f:


        writer(f).writerow( [new_isbn, author_name, book_title] )

        print('\nAdded was successfully!\n\n')

# Transfer a single book row by ISBN from one CSV file to another (append only)
def transfer_book(isbn, trans_from_file, trans_to_file):

    # Load the source CSV into a pandas DataFrame with string dtype to avoid numeric coercion
    data = pandas.read_csv(trans_from_file, dtype= str)

    # Select the row(s) where isbn column equals the requested isbn and take the first match
    book = data [data['isbn'] == isbn].iloc[0]

    # Defensive: if the selection produced an empty series, inform user and return
    if book.empty:

        print(f"ISBN not found")

        return

    else:
        # Extract the values from the selected row
        exist_isbn = book["isbn"]
        author = book['author']
        title = book['book_title']

        # Open destination CSV in append mode and write the row
        with open( trans_to_file, 'a', newline= "") as f:

            writer(f).writerow( [exist_isbn, author, title])

# Remove rows that match an ISBN from a CSV file by rewriting the file without that row
def remove_book(isbn, filename):

    # Read the CSV into a DataFrame with all columns as strings
    data_file = pandas.read_csv(filename, dtype= str)

    # Keep only rows where isbn does not match the provided isbn (effectively deleting the match)
    newdata_fram = data_file[data_file['isbn'] != isbn]

    # Write the updated DataFrame back to the same CSV file without the index column
    newdata_fram.to_csv(filename, index=False)

# Display the contents of a CSV in a readable pandas table; wait for Enter to return
def display(file):

    # If the CSV has zero rows, inform the user
    if len(pandas.read_csv(file)) == 0:

        print("\nContent is emtpty!\n\n")
    else:
        # Read the CSV into a DataFrame; dtype=str avoids type surprises
        data = pandas.read_csv(file, dtype= str)

        # Replace default index with a 1-based index for easier reading by beginners
        data.index = pandas.RangeIndex(start=1, stop=len(data) + 1, step=1)
        
        print(data)

        input("\n\n### Press Enter to continue.......\n\n")


# Add a new book into library.csv after validating ISBN, title and author
def add_book():

    # Prompt user for ISBN value as text
    isbn = input('\nEnter ISBN:  ')

    # ISBN must be digits only; otherwise inform user and return early
    if not isbn.isdigit():
     
        print(f'\nISBN ({isbn}) some field are not digits!\n') 
     
    # Check library for ISBN collision
    elif is_isbn_exist(new_isbn= isbn, filename= library):

        
        print(f"\nISBN: [ {isbn} ] is already exist!\n\n")

    # Check checked-out file for ISBN collision
    elif is_isbn_exist(new_isbn= isbn, filename= checked_out_books):

        print(f"\nISBN: [ {isbn} ] is already checked out1\n\n")

    else: 

        # Prompt for book title and transform to title case for consistent display
        title = input('\nEnter title of book:  ').title()

        # Ensure title length is reasonable
        if len(title) < 2:

            print(f"\nMaybe forgot entry?\n\n")

            return

        # Validate each character in the title: allow letters, spaces and apostrophes
        for letter in title:
            
            if letter.isalpha() or letter == ' ' or letter == "'":

                continue

            else:

                print(f"\nTitle input ({letter}) is not character: ")

                return

    
        # Prompt for author name and capitalize first character for stable formatting
        author = input('\nEnter a name of author:  ').capitalize()

        # Minimal length check for author
        if len(author) < 2:

            print(f"\nMaybe forgot enter a name?\n\n")

            return
        
        # Validate author characters similarly to title
        for letter in author:

            if letter.isalpha() or letter == ' ' or letter == "'":
                continue

            else:
                print(f'\nName entry [ {letter} ] is not character!\n\n ')

                return

        # All validations passed: append new row to library CSV
        store_data(new_isbn= isbn, author_name= author, book_title= title)

# Check out a book: move it from library.csv to checked-out.csv after validations
def check_out():

    # If library is empty, nothing to check out
    if len(pandas.read_csv(library)) == 0:

        print('There are no books to borrow\n\n')

        return

    # Prompt for ISBN to check out
    isbn = input('Etner ISBN:  ')

    # Validate ISBN digits
    if not isbn.isdigit(): 

        print(f'\nTry again, your entry [ {isbn} ] is not isbn digits\n\n')

        return

    # If ISBN is not present in library, show available books and return
    if not is_isbn_exist(new_isbn= isbn, filename= library):

        print(f"\nThis ISBN ({isbn}) is not definde or already checked out\n\n")

        print(f"Available books:\n____________\n")

        display(file= library)

        return

    # If ISBN exists in library and not already in checked-out file, transfer it
    if not is_isbn_exist(new_isbn= isbn, filename= checked_out_books):

        # Transfer the entry to checkedout_books
        transfer_book(isbn= isbn, trans_from_file= library, trans_to_file= checked_out_books)

        print(f'\nISBN: [ {isbn} ] Checkedout successful!\n\n') 

        # Remove the transferred row from library.csv so it's no longer available
        remove_book(isbn= isbn, filename= library)
        
    else:
        # If already checked out, inform the user
        print(f"\nISBN: [ {isbn} ] is laready checked out!\n\n")

# Check in a book: move it back from checked-out.csv to library.csv after validations
def check_in():

    # If checked-out file is empty, nothing to check in
    if len(pandas.read_csv(checked_out_books)) == 0:

        print('\nNo books checked out of library\n\n')

    else:
        # Prompt for ISBN to check in
        isbn = input('\nEnter ISBN:  ')

        # Validate digits
        if not isbn.isdigit():

            print(f'\nYour input ({isbn}) is not digit!\n\n')

            return
        # Prevent duplicates: if ISBN already exists in library, do not move it
        if is_isbn_exist(new_isbn= isbn, filename= library):

            print(f"\nISBN [ {isbn} ] is already exist in library!\n\n")

            return
            
        # If ISBN not in checked-out collection, show borrowed books and return
        if not is_isbn_exist(new_isbn= isbn, filename= checked_out_books):

            print(f'\nISBN ({isbn}) did not check out or not definde\n\n')

            print(f"Borrowed books to check in:\n__________\n")

            display(file= checked_out_books)

            return

        # Transfer the row from checked-out back to library and then remove from checked-out
        transfer_book(isbn= isbn, trans_from_file= checked_out_books, trans_to_file= library)

        remove_book(isbn= isbn, filename= checked_out_books)

        print(f'\nISBN [ {isbn} ] checked in is successfully\n\n')

# Delete data permanently
def del_data(file_path):


        data_file = pandas.read_csv(file_path, nrows=0) 
        
        # Create an empty DataFrame using the columns (header) from the original file.
        df_empty = pandas.DataFrame(columns=data_file.columns)
        
        # Write the empty DataFrame back to the original file path.
        # index=False ensures the row index is not written.
        df_empty.to_csv(file_path, index=False)
        
        print(f"Successfully emptied data from: {file_path}")

# Print the CLI menu options for the user
def show_menu_choices():
    """
    Print the menu of available actions."""

    print('''
        1. Add book
        2. Check out book
        3. Check in book
        4. Show available books
        5. Show borrowed books
        6. Dlete all data
        7. EXIT ‼️''')

# Main program entrypoint to ensure files exist and run the menu loop
def main():

    # Create files with header row if they are missing
    generate_file(file_name= library)

    generate_file(file_name= checked_out_books)

    # Start the interactive CLI loop
    while True:

        clear_terminal()

        show_menu_choices()
        
        # Prompt user for a numeric choice
        choice_option = input('\nEnter your chioce:  ')

        # Validate that the choice is a single digit string
        if not choice_option.isdigit() or len ( choice_option ) > 1:

            print(f'\nEnter a digit from [ 1 to 7 ] please, not [ {choice_option} ]\n\n')

        else:
            clear_terminal()

            # Convert the validated choice to an integer
            int_option = int(choice_option) 

            # Map choices to functions
            if int_option == 1: # Add book

                add_book()

            elif int_option == 2: # Check out

                check_out()

            elif int_option == 3: # Check in

                check_in()

            elif int_option == 4: # Display availabel books

                display(file= library)

            elif int_option == 5: # Display borrow books

                display(file= checked_out_books)

            elif int_option == 6: # Delete data

                # Only attempt deletion if either file contains rows
                if len(pandas.read_csv(library)) == 0 and len(pandas.read_csv(checked_out_books)) == 0:

                    print(f'\nContent is already empty\n\n')

                else:

                    # Delet content
                    del_data(file_path= library)
                    del_data(file_path= checked_out_books)
                    input("\n\nPress enter to continue.....  ")


            elif int_option == 7: # Stop running

                print("\nSee you later!\n\n")

                break

            else: # Invalid entry

                print(f"Please enter a digit from [ 1 to 7 ] not [ {choice_option} ]\n\n")

        # Pause briefly so the user can read the result before the menu reappears
        sleep(3)

# Run the program when the module is executed directly
main()

# Resolved use cases (Done***):

# - Remove a book from library when it is borrowed (transfer + delete) [Done *****]
# - Add ISBN and all book metadata to checked-out file when checking out [Done ***]