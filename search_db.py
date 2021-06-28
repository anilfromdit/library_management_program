import pandas as pd
import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()


def book_search():
    search = input("Enter Search Query For Searching Books:")
    if not search.isnumeric():
        search = search.upper()
    cursor.execute("SELECT * FROM books WHERE Book_Name = ? OR Author_name = ? OR Publication = ? OR Genre = ? OR ISBN=?",
                   (search, search, search, search, search.lower()))
    book_search_result = cursor.fetchall()
    if book_search_result:
        df = pd.DataFrame(book_search_result)
        df = df.rename({0: "Book Name", 1: "Author Name",
                       2: "Publisher", 3: "Genre", 4: "ISBN", 5: "Stock"}, axis=1)
        df.index = df.index + 1
        print(df)
        input("Hit Enter To Return To Main Menu")

    else:
        opt = input(
            f"Can't Find Any Result Using '{search}'.Do You Want To Retry With Other Keyword?[y/n]  ")
        if opt.lower() == 'y':
            book_search()

    return


def member_search():
    search = input("Enter Search Query For Searching User:")
    if not search.isnumeric():
        search = search.upper()
    cursor.execute("SELECT * FROM users WHERE f_name = ? OR l_name = ? OR username = ? OR mob_num = ? OR city = ?",
                   (search, search, search.lower(), search, search))
    user_search_result = cursor.fetchall()
    if user_search_result:
        df = pd.DataFrame(user_search_result)
        df = df.rename({0: "First Name ", 1: "Last Name ",
                       2: "username  ", 3: "  Mob. Number", 4: "City"}, axis=1)
        df.index = df.index + 1
        print(df)
        cursor.execute("SELECT username FROM users WHERE f_name = ? OR l_name = ? OR username = ? OR mob_num = ? OR city = ?",
                   (search, search, search.lower(), search, search))
        username=cursor.fetchone()
        cursor.execute("SELECT Book_Name FROM issued_books WHERE username = ?",(username[0],))
        df=cursor.fetchall()
        if df:
            print(f"These Are The Issued Book(s) To {username[0]}:")
            df = pd.DataFrame(df)
            df = df.rename({0: "  Book Name"}, axis=1)
            df.index = df.index + 1
            print(df)
        else :
            print(f"These is No Issued Book(s) To {username[0]} :(")


        input("\nHit Enter To Return To Main Menu")
    else:
        opt = input(
            f"Can't Find Any Result Using '{search}'.Do You Want To Retry With Other Keyword?[y/n]  ")
        if opt.lower() == 'y':
            book_search()
    return
