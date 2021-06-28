import sqlite3
from dateutil.relativedelta import relativedelta
connection = sqlite3.connect("library.db")
import pandas as pd
from datetime import datetime
cursor = connection.cursor()
def book_issue_final(book, member):
    cursor.execute("select stock FROM books WHERE Book_Name = ? OR ISBN=?",(book.upper(), book,))
    stock = cursor.fetchone()
    cursor.execute("select Book_Name FROM books WHERE  Book_Name = ? OR ISBN = ?",
                   (book.upper(), book,))
    book_name = cursor.fetchone()
    book_name=book_name[0]
    if int(stock[0]) > 0:
        cursor.execute("SELECT username FROM users WHERE username = ? OR mob_num = ?", (member.lower(), member,))
        username=cursor.fetchone()
        username=username[0]
        cursor.execute("SELECT * FROM issued_books WHERE username = ? AND Book_Name = ?",(username,book_name,))
        flag=cursor.fetchall()
        if flag:
            print(f"{book_name} is already issued to {username}\nWe can't issue same book more than once to a member\n")
            return 0
        issue_date=datetime.now().strftime("%d/%m/%Y")
        return_date=(datetime.now()+relativedelta(days=14)).strftime("%d/%m/%Y")
        
        cursor.execute("INSERT INTO issued_books VALUES(?,?,?,?)",(username,book_name,issue_date,return_date))
        connection.commit()
        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute(
            "UPDATE books SET stock = stock - 1 WHERE Book_Name =?", (book_name,))
        connection.commit()
        return 1
    else:
        print("Oops, We're Out of Stock for that book.\nIs There pending book returns? \nConsidered Maintaining Stock Before Issuing More Books")
        return 0
    

def book_issue_book_check(member):
    book = input("Enter which book is to be issued:")
    cursor.execute("select * FROM books WHERE  Book_Name = ? OR ISBN = ?",
                   (book.upper(), book,))
    book_result = cursor.fetchall()
    if len(book_result) == 1:
        print("One Result Found:\n")
        df = pd.DataFrame(book_result)
        df = df.rename({0: "Book Name", 1: "Author Name",
                       2: "Publisher", 3: "Genre", 4: "ISBN", 5: "Stock"}, axis=1)
        df.index = df.index + 1
        print(df)
        con = input("\nDo You Continue?[Y/n] ")
        if con.lower() == 'y':
            val=book_issue_final(book, member)
            if val == 0:
                return 0
            elif val == 1:
                return 1

        else:
            return 0
    elif len(book_result) > 1:
        print("Multiple Result Found:")
        df = pd.DataFrame(book_result)
        df = df.rename({0: "Book Name", 1: "Author Name",
                       2: "Publisher", 3: "Genre", 4: "ISBN", 5: "Stock"}, axis=1)
        print(df)
        input("\nUse other options to search for Book\nHit Enter To Return To Main Menu")
        return 0
    else:
        print("Oops, No Book Found, Please Try Again")
        return 0

def book_issue_user_check():
    count =0
    member = input("Enter member's username or contact number:")
    cursor.execute(
        "SELECT * FROM users WHERE username = ? OR mob_num = ?", (member.lower(), member,))
    member_result = cursor.fetchall()
    if len(member_result) == 1:
        print("One Result Found:\n")
        df = pd.DataFrame(member_result)
        df = df.rename({0: "First Name ", 1: "Last Name ",
                       2: "username  ", 3: "  Mob. Number", 4: "City"}, axis=1)
        df.index = df.index + 1  
        print(df)
        con = input("\nDo You Continue?[Y/n] ")
        if con.lower() == 'y':
            val=book_issue_book_check(member)
        else:
            print("Operation: Book Issue Has Been Cancelled")
            input("Hit Enter To Continue")
            return
    elif len(member_result) > 1:
        df = pd.DataFrame(member_result)
        df = df.rename({0: "First Name ", 1: "Last Name ",
                       2: "username  ", 3: "  Mob. Number", 4: "City"}, axis=1)
        print(df)
        input("Use other options to search for member or modify member details\nHit Enter To Return To Main Menu")
        return
    else:
        input("Oops, No Member Found, Please Try Again\nHit Enter To Return To Main Menu")
        return
    while 1:
        if val ==0:
            input("Operation: Book Issue Has Been Cancelled\nHit Enter To Return To Main Menu")
            return
        if val==1:
            count+=1
            more=input(f"Is There More Books To Be Issued To {member}?[Y/n]  ")
            if more.lower() == 'y':
                book_issue_book_check(member)
            else :
                print(f"{count} Book(s) Has Been Successfully Issued to {member}")
                input("Hit Enter To Return To Main Menu")
                return
        


    
    
