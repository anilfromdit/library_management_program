from book_return import book_return_book_check
import sqlite3
connection= sqlite3.connect("library.db")
cursor= connection.cursor()
import pandas as pd
from playsound import playsound
def del_member():
    username=input("Enter member's username you wish to delete:").lower()
    cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
    username_result=cursor.fetchall()
    if len(username_result)==0:
        print(f"Oops,No user found with username {username}")
        ret=input("Do You Want To Retry?[Y/n]  ")
        if ret.lower() == 'y':
            del_member()
        return
    username_result=pd.DataFrame(username_result)
    username_result = username_result.rename({0: "First Name ", 1: "Last Name ",2: "username  ", 3: "  Mob. Number", 4: "City"}, axis=1)
    username_result.index = username_result.index + 1
    print(username_result)
    con=input("Do you want to continue?[Y/n]  ")
    if con.lower() !='y':
        input("Operation: Delete User Has Been Cancalled\nHit Enter To Continue")
        return
    username_result=cursor.execute("SELECT * FROM issued_books WHERE username=?",(username,)).fetchall()
    while(len(username_result)):
        if len(username_result)!=0:
            con=input(f"There Are Some Books Issued To {username}\nDo You Want To Delete Them?[Y/n]   ") 
            if con =='y':
                book_return_book_check(username)
            else:
                return
            username_result=cursor.execute("SELECT * FROM issued_books WHERE username=?",(username,)).fetchall()
    cursor.execute("DELETE FROM users WHERE username=?",(username,))
    print("Processing Your Request...")
    connection.commit()
    playsound('sounds\del.mp3')
    input("Member Deleted Successfully\nHit Enter To Return To Advance Menu")
