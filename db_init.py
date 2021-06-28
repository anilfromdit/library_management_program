import sqlite3
connection= sqlite3.connect("library.db")
cursor= connection.cursor()

sql_command = """
        CREATE TABLE IF NOT EXISTS books(
            Book_Name VARCHAR(64) NOT NULL ,
            Author_name VARCHAR(64) NOT NULL ,
            Publication VARCHAR(64) NOT NULL ,
            Genre VARCHAR(64) NOT NULL ,
            ISBN VARCHAR(64) NOT NULL ,
            stock DECIMAL
        );"""
cursor.execute(sql_command)
sql_command = """
        CREATE TABLE IF NOT EXISTS users(
            F_name VARCHAR(64) NOT NULL,
            L_name VARCHAR(64) NOT NULL,
            username VARCHAR(64) NOT NULL ,
            Mob_num VARCHAR(10) NOT NULL ,
            City VARCHAR(16) NOT NULL
        );"""
cursor.execute(sql_command)
sql_command = """
        CREATE TABLE IF NOT EXISTS issued_books(
            username VARCHAR(64) NOT NULL,
            Book_Name VARCHAR(64) NOT NULL,
            Issue_Date text,
            Due_Date text

        );"""
cursor.execute(sql_command)
sql_command="""
CREATE TABLE IF NOT EXISTS late_return(
    Username VARCHAR(64) NOT NULL,
    Book_Name VARCHAR(64) NOT NULL,
    Issue_Date text,
    Due_Date text,
    Fine_Collected int(10),
    Remarks VARCHAR(256)
    );"""
cursor.execute(sql_command)
sql_command="""
CREATE TABLE IF NOT EXISTS Accounts(
    username VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL
    );"""
cursor.execute(sql_command)

connection.commit()
