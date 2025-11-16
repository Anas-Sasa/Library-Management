# #*****************( BOOK GALARY ) [ 3 JLUI 2024 ]

import os 
import random

library = {}

check_out_books = {}

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def add_book():
    global library

    check_varible = False
    
    isbn_num = input('\nEnter ISBN:  ')

    if not isbn_num.isdigit():
     
     print(f'\nISBN ({isbn_num}) some field is not a digit:***') 

    elif isbn_num in library:

        print(f"\nISBN ({isbn_num}) is already in library:**")

    else:

        title_of_book = input('\nEnter title of book:  ').title()
  
        for letter in title_of_book:

            if letter.isalpha() or letter == ' ':
                continue

            else:

                print(f"\nTitle input ({letter}) is not lapha letter: ")
                check_varible = '0'
                break

        if check_varible == '0': 

            print('\nTry again')

        elif not title_of_book:

            print('\nMaby you forgot to enter data:***')

        else:

            author = input('\nEnter a name of author:  ').capitalize()
         
            for letter in author:
                if letter.isalpha() or letter == ' ':
                    continue
                else:
                    print(f'\nAuthor entry ({letter}) is not alpah letter:  ')
                    check_varible = '0'
                    break
        

            if check_varible == '0':
                print('\nTry again:**')

            elif not author:
                print(f'\nMaby you forgot to enter data:***')

            else:
                library[isbn_num] = {
                    'author':[author],
                    'title':[title_of_book],
                }
                check_varible = True

    print('Added was successfully:***') if check_varible == True else print('Added was not successfully:***')



while True:
    print('''
          1. ADD BOOK 
          2. CHECK OUT BOOK 
          3. CHECK IN BOOK 
          4. SHOW AVAILABLE BOOKS
          5. SHOW BORROW BOOKS
          6. Dlete data
          7. EXIT 
 ''')
    choice_option = input('Enter your chioce:  ')

    if not choice_option.isdigit():

        print(f'\nYour entry ({choice_option}) is not a digit:**')

    else:

        clear_screen()
        int_choice = int(choice_option)

        if int_choice == 1:
            add_book()

        elif int_choice == 2:

            if not library:

                print('There are no books to borrow:***')

            else:

                isbn_num = input('Etner ISBN number:  ')

                if not isbn_num.isdigit(): 
                    print(f'\nTry again, your entry ({isbn_num}) is not digit:')

                else:

                    if isbn_num not in library:

                        print(f"This ISBN ({isbn_num}) is not definde or already checked out:***")

                    else:

                        # HOW TO ADD ISBN IN OUT_CHECK_DIC WITH ALL OF DATA? (Done***)
                        print('ISBN.',isbn_num,library[isbn_num],': checked out of the library:***') 
                        
                        for data_in_isbn in library[isbn_num]:

                            for info in library[isbn_num][data_in_isbn]:

                                if isbn_num not in check_out_books:

                                    check_out_books[isbn_num] = {data_in_isbn : [info],} 

                                else:
                                    check_out_books[isbn_num][data_in_isbn] = [info]

                        if library[isbn_num] == check_out_books[isbn_num]:

                            del library[isbn_num]

                            print(f'Checked out ISBN ({isbn_num}) is successfully:***')

                        else:
                            print(f'Checked out ISBN ({isbn_num}) was not successfully:***')

        elif int_choice == 3:

            if not check_out_books:

                print('\nNo books checked out of library:***')

            else:
                isbn_num = input('\nEnrer ISBN number:  ')

                if not isbn_num.isdigit():

                    print(f'\nYour input ({isbn_num}) is not digit:***')

                else:

                    if not isbn_num in check_out_books:
                        print(f'\nISBN ({isbn_num}) did not check out or not definde:***')

                    else:

                        for data_in_isbn in check_out_books[isbn_num]:

                            for info in check_out_books[isbn_num][data_in_isbn]:

                                if isbn_num not in library:

                                    library[isbn_num] = {data_in_isbn: [info],}

                                else:
                                    library[isbn_num][data_in_isbn] = [info]

                        if check_out_books[isbn_num] == library[isbn_num]:

                            del check_out_books[isbn_num]

                            print(f'\nISBN ({isbn_num}) checked in is successfully:***')

                        else:
                            print(f'\nISBN ({isbn_num}) checked in was not successfully:***')
                
        elif int_choice == 4:

            if not library:
                print('\nlibrary is empty there is nothing to show:') 

            else:
                print('\n***Available Books***\n')
                for keys in library:
                    print('ISBN.',keys,': ',library[keys])
                    print('- - - - - - - -')

        elif int_choice == 5:

            if not check_out_books:
                print(f'Out check list is empty: ({check_out_books} ***)')

            else:
                print('\n***Books out of library***\n')
                for keys in check_out_books:
                    print('ISBN: ',keys,check_out_books[keys])
                    print('- - - - - - - - - ')

        elif int_choice == 6:
            if not library:
                print(f'Library is already empty: ({library}) ***')

            else:
                library = {}
                print(f'\nDeleted was successfully: library {library} ***')

        elif int_choice == 7:
            break
        else:
            print(f'\nYour entry ({choice_option}) is more than a field:') if len(choice_option) >1 else print(f'\nYour entry ({choice_option}) is out of range')

# (9 JULI FINISHED PRODUCT )***






