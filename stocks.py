import sqlite3
import pandas as pd
connection= sqlite3.connect("library.db")
cursor= connection.cursor()
def print_stock():
    print("Here's The Library Stock:")
    stock=pd.read_sql_query("SELECT * FROM books",connection)
    stock.index = stock.index + 1 
    if len(stock) == 0:
        print("Oops, We're Out of Stock :(")
    else:
        print(stock)
    input("\n\nHit Enter To Return To Main Menu")

def print_issued_books_data():
    print("\n\nHere's The Issued Books Data:")
    stock=pd.read_sql_query("SELECT * FROM issued_books",connection)
    stock=stock.rename({"username":"   username   ","book_name":"   Book Name"},axis=1)
    stock.index = stock.index + 1
    if len(stock) == 0:
        print("There's No Book Issued Yet :(")
    else:
        print(stock)
    input("\n\nHit Enter To Return To Main Menu")

def print_fine_collection():
    collection=pd.read_sql_query("SELECT * FROM late_return",connection)
    collection.index = collection.index + 1
    if len(collection) == 0:
        print("our member's are punctual so no collection yet :)")
    else:
        print(collection)
    input("\n\nHit Enter To Return To Main Menu")