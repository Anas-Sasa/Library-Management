# ( BOOKS LIBRARY ) --> Editing on [ 16 Nov 2025 ]

import os, time

library = {}

checkedout_books = {}

def sleep(duration):
    time.sleep(duration)


def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def add_book():

    check_varible = True
    
    isbn = input('\nEnter ISBN:  ')

    if not isbn.isdigit():
     
     print(f'\nISBN ({isbn}) some field is not a digit:***') 

    elif isbn in library:

        print(f"\nISBN ({isbn}) is already in library:**")

    elif isbn in checkedout_books:

        print(f"\nISBN [ {isbn} ] is already exist in checkedout\n\n")

    else: 

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


        if check_varible:

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
        

            if check_varible:

                library[isbn] = {
                    'author':[author],
                    'title':[title_of_book],
                }
                

        if check_varible:
            print('\nAdded was successfully!\n\n')

        else:
            print('\nAdded was not successfully!\n\n')


def check_out():

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

        # HOW TO ADD ISBN IN OUT_CHECK_DIC WITH ALL OF DATA? (Done***)
        if isbn_num not in checkedout_books:

            checkedout_books[isbn_num] = library[isbn_num]


            print('\n\nISBN: ',isbn_num,library[isbn_num],'\n\nCheckedout successful!\n\n') 

            del library[isbn_num]


def check_in():


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

            library[isbn_num] = checkedout_books[isbn_num]

            print(f'\nISBN ({isbn_num}) checked in is successfully\n\n')
                
            del checkedout_books[isbn_num]


def dispaly(dict):

    for isbn in dict:
        
        for data in dict[isbn]:

            print(f'ISBN: {isbn}: {dict[isbn]}\n')
            print('_' * 20)
            print("\n")
            break

def show_choices():

    print('''
        1. ADD BOOK 
        2. CHECK OUT BOOK 
        3. CHECK IN BOOK 
        4. SHOW AVAILABLE BOOKS
        5. SHOW BORROW BOOKS
        6. Dlete data
        7. EXIT 
''')


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
                print('\n***Available Books***\n')

                dispaly(dict= library)

        elif int_option == 5: # display borrow books

            if not checkedout_books:

                print(f'\nNothing checkedout! [ {checkedout_books} ]\n\n')

            else:
                print('\n\n---Checkedout books---\n\n')


                dispaly(dict= checkedout_books)


        elif int_option == 6:

            if not library:

                print(f'\nLibrary is already empty: [ {library} ]\n\n')

            else:
                library = {}
                print(f'\nDeletion was successfully: [ {library} ]\n\n')

        elif int_option == 7:
            print("\nSee you later!\n\n")
            break

        else:

            print(f"Please enter a digit from [ 1 to 7 ] not [ {choice_option} ]\n\n")
    
    sleep(3)

