import sqlite3
import pandas as pd
connection= sqlite3.connect("library.db")
cursor= connection.cursor()
def print_member_data():
    try:
        print("Here's The List Of Members:\n")
        df=pd.read_sql_query("SELECT * FROM users",connection)
        df = df.rename({"F_name": "First Name ", "L_name": "Last Name ","username": "username  ", "Mob_num": "  Mob. Number", 4: "City"}, axis=1)
        df.index = df.index + 1
        if len(df) == 0:
            print("Oops, No Member Yet.. :(")
        else:
            print(df)
        
    except:
        print("Oops, An Error occurred, Please Try Again")
    
    input("\n\nHit Enter To Continue")
