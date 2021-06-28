from os import system
from add_book import add_book
from add_member import add_member
from book_issue import book_issue_user_check
from book_return import book_return_user_check
from search_db import book_search,member_search
from stocks import print_stock,print_issued_books_data,print_fine_collection
from del_book import del_book
from del_member import del_member
from member_list import print_member_data
from update_member import update_member
import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()


def opt_validator(opt):
    if opt == 1:
        add_book()
    elif opt == 2:
        add_member()
    elif opt == 3:
        book_issue_user_check()
    elif opt == 4:
        book_return_user_check()
    elif opt == 5:
        book_search()
    elif opt == 6:
        print_stock()
    elif opt == 7:
        print_issued_books_data()
    elif opt ==8:
        print_fine_collection()
    elif opt ==9:
        del_book()
    elif opt == 10:
        del_member()
    elif opt == 11:
        print_member_data()
    elif opt == 12:
        update_member()
    elif opt ==13:
        member_search()
    

def advance_menu():
    while(1):
        system("cls")
        print("****Advance Menu****")
        print("""
     1. To Print Fine Collection Data
     2. To Delete A Book
     3. To Delete A Member
     4. To Print Members Details
     5. To Update Member Details
     6. To Search Member Details
     7. Main Menu
     8. Log Out 
     9. EXIT
    """)
        opt=input("Enter Your Choice:")
        if(opt)=='':
            advance_menu()
            return
        elif opt.lower() == 'logout' or opt.lower()=='log out' or opt == '8':
            return 'logout'
        elif opt.lower() == 'exit' or opt == '9':
            print("Thank You For Using This Program\nThis Program Was Made By Anil Gulati\n@anilfromdit")
            exit()
        elif int(opt) == 7:
            return
        elif int(opt) > 0 and int(opt) < 7:
            opt_validator(int(opt)+7)
        else:
            print("That's An Invalid Input\nDo You Want To Retry?[Y/n] ")
            retry=input()
            if(retry.lower()!='y'):
                return

def menu():
    while(1):
        system("cls")
        print("********  Main Menu  ********")
        print('''  
    1. To Add Book
    2. To Add Member
    3. To Issue A Book
    4. To Return Issued Book
    5. To Search A Book
    6. To Print Available Stock
    7. To Print Issued Books Data
    8. Advance
    9. Log Out
   10. EXIT
        ''')
        opt = input("Enter Your Choice:")
        try:
            if(opt)=='':
                menu()
            elif opt.lower() == 'logout' or opt.lower()=='log out' or opt =='9':
                return
            elif opt.lower() == 'exit' or opt == '10':
                print("Thank You For Using This Program\nThis Program Was Made By Anil Gulati\n@anilfromdit")
                exit()
            elif int(opt) == 8:
                val=advance_menu()
                if val=='logout':
                    return
            elif int(opt) > 0 and int(opt) < 9:
                opt_validator(int(opt))
        except ValueError:
                print("That's An Invalid Input\nDo You Want To Retry?[Y/n] ")
                retry=input()
                if(retry.lower()!='y'):
                    print("Thank You For Using This Program\nThis Program Was Made By Anil Gulati\n@anilfromdit")
                
