import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()
from playsound import playsound
def del_book():
    name=input("Enter Book Title:")
    if name.lower() == 'exit':
        print("Operation: BOOK DELETION HAS BEEN CANCELLED")
        input("Hit Enter To Continue")
        return
    name=name.upper()
    cursor.execute("SELECT * FROM issued_books WHERE Book_Name = ?",(name,))
    con=cursor.fetchall()
    if len(con) == 0:
        cursor.execute("SELECT rowid FROM books WHERE Book_Name = ?", (name,))
        data=cursor.fetchall()
        if len(data)==0:
            print(f'There is No Book Titled: {name}')
            input("Hit Enter To Continue")
            return
        print("Processing Your Request...")
        playsound('sounds\del.mp3')
        cursor.execute("DELETE FROM books WHERE Book_Name=?",(name,))
        connection.commit()
        print(f"Successfully Deleted {name} from record")
        
    else:
        print(f"Book Titled: '{name}' is issued To Someone, can't delete book with pending returns")
    input("Hit Enter To Continue")
    