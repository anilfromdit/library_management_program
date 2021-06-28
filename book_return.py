import sqlite3
import functools
import operator
connection = sqlite3.connect("library.db")
import pandas as pd
from datetime import datetime
cursor = connection.cursor()
def book_return_book_check(username):
    r=0
    cursor.execute("SELECT Book_Name FROM issued_books WHERE username = ?",(username,))
    book=cursor.fetchall()
    if len(book) == 0:
        print(f"There's No Book Issued To {username}")
        return 0
    elif len(book) == 1:
        print(f"There's One Book Issued To {username}")
        df = pd.DataFrame(book)
        df = df.rename({0: "  Book Name"}, axis=1)
        df.index = df.index + 1 
        print(df)
        book=book[0]
        con=input("Do You Want To Continue?[Y/n]  ")
        if con.lower()=='y':
            cursor.execute("SELECT issue_date FROM issued_books WHERE  Book_Name=? AND username = ?",(book[0],username))
            issue_date=cursor.fetchone()
            cursor.execute("SELECT due_date FROM issued_books WHERE  Book_Name=? AND username = ?",(book[0],username))
            due_date=cursor.fetchone()
            date_format = "%d/%m/%Y"
            issue_date=functools.reduce(operator.add, (issue_date))
            due_date=functools.reduce(operator.add, (due_date))
            today=datetime.now().strftime("%d/%m/%Y")
            a=datetime.strptime(today,date_format)
            b=datetime.strptime(due_date,date_format)
            delta=a-b
            late=delta.days
            if late>0:
                fine=int(late)*2
                print(f"Due Date To Return {book[0]} was: {due_date} But {username} is {late} Day(s) Late\nkindly Collect RS.{fine} Fine From {username}")
                collect=input(f"Have You Collected Rs.{fine}?[Y/n]  ")
                if collect.lower() != 'y':
                    print("Operation: Return Book Has Been Cancelled")
                    return 0
                ask=input("Do You Want To Add Any Remark To This Fine Collection?[Y/n]  ")
                if ask.lower()=='y':
                    remarks=input("Enter Your Remarks:")
                else:
                    remarks=" "
                params=(username,book[0],issue_date,due_date,fine,remarks)
                cursor.execute("INSERT INTO late_return VALUES(?,?,?,?,?,?)",params)


            cursor.execute("DELETE FROM issued_books WHERE Book_Name=? AND username = ?",(book[0],username))
            connection.commit()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute("UPDATE books SET stock = stock + 1 WHERE Book_Name =?", (book[0],))
            connection.commit()
            return 1
    elif len(book) > 1:
        print(f"There Are Multiple Books Issued To {username}:")
        df = pd.DataFrame(book)
        df = df.rename({0: "  Book Name"}, axis=1)
        df.index = df.index + 1
        print(df)
        try:
            book_id=int(input("\nEnter Your Choice:"))
            book=book[book_id-1]
            cursor.execute("DELETE FROM issued_books WHERE Book_Name=? AND username = ?",(book[0],username))
            connection.commit()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute("UPDATE books SET stock = stock + 1 WHERE Book_Name =?", (book[0],))
            connection.commit()
            return 1
        except:
            print("Invalid Input")
            return 0

def book_return_user_check():
    count =0
    user=input("Enter detail of member who wants to return a book:")
    cursor.execute("SELECT username FROM users WHERE username = ? OR mob_num = ?", (user.lower(), user,))
    username2 = cursor.fetchall()
    if len(username2) == 1:
        username=username2[0]
        print("\nOne Result Found:")
        username=str(username)
        username=username.split('\'')[1]
        df = pd.DataFrame(username2)
        df = df.rename({0: "ID  ", 1: "First Name ", 2: "Last Name ",
                       3: "username  ", 4: "  Mob. Number", 5: "City"}, axis=1)
        df.index = df.index + 1 
        print(df)

        con = input("\nDo You Continue?[Y/n] ")
        if con.lower() == 'y':
            val=book_return_book_check(username)
            while 1:
                if val==0:
                   input("Hit Enter To Return To Main Menu")
                   return 0
                if val == 1:
                    count+=1
                    more=input(f"Is There More Books To Be returned by {username}?[Y/n]  ")
                    if more.lower() == 'y':
                        book_return_book_check(username)
                    else :
                        print(f"{count} Book(s) Has Been Successfully Returned By {username}")
                        input("Hit Enter To Return To Main Menu")
                        return 1

        else:
            print("Operation: Book Return Issue Has Been Cancelled")
            input("Hit Enter To Continue")
            return
    elif len(username2) > 1:
        print("Multiple Result Found:")
        df = pd.DataFrame(username2)
        df = df.rename({0: "ID  ", 1: "First Name ", 2: "Last Name ",
                       3: "username  ", 4: "  Mob. Number", 5: "City"}, axis=1)
        df.index = df.index + 1
        print(df)
        input("\nUse other options to search for member or modify member details\nHit Enter To Return To Main Menu")
        return
    else:
        input("Oops, No Member Found, Please Try Again\nHit Enter To Return To Main Menu")
        return
