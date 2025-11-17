"""
library_cli.py

Simple command-line Books Library manager.

Provides functions to add books, check them out, check them back in, and
display library or checked-out collections. Data is stored in-memory using
two dictionaries: `library` for available books and `checkedout_books` for
borrowed books.

Note: This is a lightweight demo for local use; there is no persistent storage.
"""

# [ BOOKS LIBRARY ] --> Editing on [ 16 Nov 2025 ]

# Standard library imports
# os: clear the terminal in a cross-platform way
# time: pause execution briefly to improve CLI readability
import os, time

# In-memory storage for available and borrowed books
library = {}
checkedout_books = {}


def sleep(duration):
    """
    Pause execution for the given number of seconds."""

    time.sleep(duration)

def clear_terminal():
    """
    Clear the terminal screen depending on the operating system."""

    os.system('clear' if os.name == 'posix' else 'cls')

def add_book():
    """
    Prompt the user to add a new book to the library.

    -Validates ISBN (digits only) and simple alphabetic checks for title and author.

    -On success, inserts an entry into the `library` dictionary with ISBN as key and
    a small info dict as value.
    """

    # Using to control valid info when want to insert bood
    check_varible = True
    
    isbn = input('\nEnter ISBN:  ')

    # ISBN must be numeric
    if not isbn.isdigit():
     
     print(f'\nISBN ({isbn}) some field are not digits!\n') 

    # ISBN must not already exist in either collection
    elif isbn in library:

        print(f"\nISBN ({isbn}) is already in library!\n")

    elif isbn in checkedout_books:

        print(f"\nISBN [ {isbn} ] is already checkedout\n\n")

    else: 
    # Title validation: minimal length and alphabetic characters / spaces only
        title_of_book = input('\nEnter title of book:  ').title()

        if len(title_of_book) < 2:

            print(f"\nMaybe forgot entry?\n\n")
            return

        for letter in title_of_book:
            
            if letter.isalpha() or letter == ' ':
                continue

            else:

                print(f"\nTitle input ({letter}) is not lapha letter: ")

                check_varible = False
                break

        # It must the took info is valid
        if check_varible:

            # Author validation: minimal length and alphabetic characters / spaces only
            author = input('\nEnter a name of author:  ').capitalize()

            if len(author) < 2:

                print(f"\nMaybe forgot entry?\n\n")
                return
            
            for letter in author:

                if letter.isalpha() or letter == ' ':
                    continue

                else:
                    print(f'\nAuthor entry ({letter}) is not alpah letter:  ')

                    check_varible = False
                    break
        
            # It must the took info is valid to insert book
            if check_varible:

                # All checks passed: add to library. Use lists so future metadata can be appended.
                library[isbn] = {
                    'author':[author],
                    'title':[title_of_book],
                }
                
                print('\nAdded was successfully!\n\n')

            else:
                print('\nAdded was not successfully!\n\n')


def check_out():
    """
    Move a book from `library` to `checkedout_books` by ISBN.

    Validates input and prints the moved entry.
    """

    if not library:

        print('There are no books to borrow\n\n')
        return


    isbn_num = input('Etner ISBN number:  ')


    if not isbn_num.isdigit(): 

        print(f'\nTry again, your entry ({isbn_num}) is not digit\n\n')
        return

    
    if isbn_num not in library:

        print(f"\nThis ISBN ({isbn_num}) is not definde or already checked out\n\n")
        return

    else:
        # HOW TO ADD ISBN IN OUT_CHECK_DIC WITH ALL OF DATA? (***Done***)

        if isbn_num not in checkedout_books:

            # Transfer the entry to checkedout_books and remove from library
            checkedout_books[isbn_num] = library[isbn_num]


            print('\n\nISBN: ',isbn_num,library[isbn_num],'\n\nCheckedout successful!\n\n') 

            del library[isbn_num]


def check_in():
    """
    Return a book from `checkedout_books` back into `library` by ISBN.

    Validates input and prevents duplicate ISBNs in library.
    """

    if not checkedout_books:

        print('\nNo books checked out of library\n\n')

    else:

        isbn_num = input('\nEnter ISBN number:  ')

        if not isbn_num.isdigit():

            print(f'\nYour input ({isbn_num}) is not digit!\n\n')
            return

        if isbn_num in library:

            print(f"\nISBN [ {isbn_num} ] is exist in library!\n\n")
            return
            
        if not isbn_num in checkedout_books:

            print(f'\nISBN ({isbn_num}) did not check out or not definde\n\n')
            return


        if isbn_num not in library:

            # Move back to library and delete isbn from checkout_books
            library[isbn_num] = checkedout_books[isbn_num]

            print(f'\nISBN ({isbn_num}) checked in is successfully\n\n')
                
            del checkedout_books[isbn_num]


def dispaly(dict):
    """
    Nicely print the contents of the provided collection (dictionary).

    Expects a mapping from ISBN -> info-dict and prints each ISBN with its info.
    """

    for isbn in dict:

        print(f"ISBN: {isbn}\n")
        # info is expected to be a dict like {'author':[...], 'title':[...]}
        for info in dict[isbn]:
            
            print(" " * 5, f"{info}: {dict[isbn][info]}\n")
            
        print("_" * 20, "\n")
            

def show_choices():
    """
    Print the menu of available actions."""

    print('''
        1. Add book
        2. Check out book
        3. Check in book
        4. Show available books
        5. Show borrowed books
        6. Dlete all data
        7. EXIT ‼️
''')

# Main CLI loop
while True:

    clear_terminal()

    show_choices()
    
    choice_option = input('\nEnter your chioce:  ')

    if not choice_option.isdigit():

        print(f'\nEnter a digit from [ 1 to 7 ] please not [ {choice_option} ]\n\n')

    else:

        clear_terminal()

        int_option = int(choice_option)

        if int_option == 1: # Add book

            add_book()

        elif int_option == 2: # Check out

            check_out()

        elif int_option == 3: # Check in

           check_in()

        elif int_option == 4: # Display availabel books

            if not library:
                print('\nLibrary is empty there is nothing to show!\n\n') 

            else:
                print('\n---Available Books---\n')

                dispaly(dict= library)

        elif int_option == 5: # Display borrow books

            if not checkedout_books:

                print(f'\nNothing checkedout! [ {checkedout_books} ]\n\n')

            else:
                print('\n\n---Checkedout books---\n\n')


                dispaly(dict= checkedout_books)


        elif int_option == 6: # Delete data

            if not library:

                print(f'\nLibrary is already empty: [ {library} ]\n\n')

            else:
                library = {}
                print(f'\nDeletion was successfully: [ {library} ]\n\n')

        elif int_option == 7: # Stop running

            print("\nSee you later!\n\n")
            break

        else: # Invalid entry

            print(f"Please enter a digit from [ 1 to 7 ] not [ {choice_option} ]\n\n")
    # Pause briefly so the user can read the result before the menu reappears
    sleep(3)
