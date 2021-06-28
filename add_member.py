import sqlite3
connection= sqlite3.connect("library.db")
cursor= connection.cursor()

def add_cancel():
    print("Operation: Adding New Member Has Been Cancelled")
    input("Hit Enter To Return To Main Menu")


def username_check(username):
    cursor.execute("SELECT rowid FROM users WHERE username = ?", (username,))
    user_check = cursor.fetchone()
    if user_check:
        print("This username is Taken, Do You Want To Retry?[Y/n]  ")
        opt = input()
        if opt.lower() == 'y':
            username=input("Assign Username:")
            opt=username_check(username)
            if opt.lower()!='cancel':
                return opt
            else:
                return "cancel"
        else:
            add_cancel()
            return "cancel"
    else:
        return username
    

def add_member():
    f_name=input("Enter First Name:")
    if(f_name.lower()=='exit'):
        add_cancel()
        return 0
    l_name=input("Enter Last Name:")
    if(l_name.lower()=='exit'):
        add_cancel()
        return 0
    username=input("Assign A Username:")
    username_validate=username_check(username)
    if(username_validate=='cancel'):
        add_cancel()
        return 0
    else:
        username=username_validate.lower()
    m_num=input("Enter Mobile Number:")
    if m_num.lower()=='exit':
        add_cancel()
        return 0
    city=input("Enter City:")
    if city.lower()=='exit':
        add_cancel()
        return 0
    params=(f_name.upper(),l_name.upper(),username.lower(),m_num,city.upper())
    try:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", params)
        connection.commit()
        print(f"User:{username} has been successfully added")
        input("Hit Enter To Continue")
    except:
        print("Oops, An Error occurred, Please Try Again")
        input("Hit Enter To Continue")




        
    