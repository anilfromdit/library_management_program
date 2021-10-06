from menu import menu
import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

def create_new_account():
    while(true):
        username = input("\nChoose A Username For Your Account:")
        if username=='':
            continue
        elif username.lower()=='exit':
            exit()
        else:
            cursor.execute("SELECT * FROM Accounts WHERE username = ?",(username.lower(),))
            allow=cursor.fetchone()
            if allow:
                print("Oops, This Username is Already Taken, Please Choose A Different One")
            else :
                break
    while(1):
        password=input("Choose A Password For Your Account:")
        if password == '':
            continue
        else:
            params=(username.lower(),password)
            cursor.execute("INSERT INTO Accounts VALUES (?,?)",params)
            connection.commit()
            input("Account Created Successfully\nHit Enter To Continue")
            return 1
def login():
    print("****** Welcome To Library Management Program ******")
    
    print("\nPlease Login To Proceed Furthur")
    username=input("Enter your Username:")
    password=input("Enter Your Password:")
    cursor.execute("SELECT * FROM Accounts WHERE username = ? AND password = ?",(username.lower(),password,))
    allow=cursor.fetchone()
    if allow:
        menu()
    else: 
        print("Oops, That's An Invalid username or password\nRemember:Passwords are Case sensitive")
        tryagain=input("Do You Want To Try Again[Y/n]  ")
        if tryagain.lower()=='y':
            login
        else :
            exit()
