import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()


def inc_stk(name):
    num = input("Enter Number of Books You Want To Increment:")
    int(num)
    try:
        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute(
            "UPDATE books SET stock = stock + ? WHERE book_name =?", (num, name,))
        connection.commit()
    except:
        print("Oops,Some Error Occurred(ERROR: X02a)")
        input("Hit Enter To Continue")


def add_cancel():
    print("Operation: Adding New Book Has Been Cancelled")
    input("Hit Enter To Return To Main Menu")


def existence_check(name):
    cursor.execute("SELECT rowid FROM books WHERE book_name = ?", (name,))
    check = cursor.fetchone()
    if check:
        print(
            "This Book Already Exist In Library\nDo You Want To Increment Stock?[Y/n] ")
        opt = input()
        if opt.lower() == 'y':
            inc_stk(name)
            return 2
        else:
            add_cancel()
            return 0

    else:
        return 1


def add_book():
    book_name = input("Enter Title of The Book:")
    book_name=book_name.upper()
    proceed = existence_check(book_name)
    if (book_name.lower()) == 'exit':
        add_cancel()
        return
    elif int(proceed) == 0:
        add_cancel()
        return
    elif int(proceed) == 2:
        print("Stock Has Been Successfully Updated")
        input("Hit Enter To Continue")
        return
    author_name = input("Enter Name of The Author:")
    if (author_name.lower()) == 'exit':
        add_cancel()
        return
    isbn = input("Enter ISBN:")
    if (isbn) == 'exit':
        add_cancel()
        return
    publication = input("Enter Name of The Publication:")
    if (publication.lower()) == 'exit':
        add_cancel()
        return
    genre = input("Enter Genre of Book:")
    if (genre.lower()) == 'exit':
        add_cancel()
        return
    num = input("Enter Number of Books:")
    if (num.lower()) == 'exit':
        add_cancel()
        return
    int(num)
    params = (book_name.upper(), author_name.upper(), publication.upper(), genre.upper(), isbn,num)
    try:
        cursor.execute("INSERT INTO books VALUES(?,?,?,?,?,?)", params)
        connection.commit()
        print(
            f"Book:{book_name} has been successfully added to stock with isbn:{isbn}")
        input("Hit Enter To Continue")
    except:
        print("Oops, An Error occurred, Please Try Again")
        input("Hit Enter To Continue")

# connection.close()
