import sqlite3
connection= sqlite3.connect("library.db")
cursor= connection.cursor()
def add_cancel():
    print("Operation: Updating Member Details Has Been Cancelled")
    input("Hit Enter To Return To Main Menu")
def user_name_search(user_name):
    user_name.lower()
    cursor.execute("SELECT rowid FROM users WHERE username = ?", (user_name,))
    username_check = cursor.fetchone()
    if username_check:
        return 1
    else:
        return 0
def update_choice(user_name):
    print("Please Choose Details To Update:")
    print("1.To Update First Name\n2.To Update Last Name\n3.To Update Mobile Number\n4.To Update City\n")
    update=input("\nEnter Your Choice:")
    if int(update)==1 or str(update).lower()=='first name':
        f_name=input("Enter First Name:")
        if(f_name.lower()=='exit'):
            add_cancel()
            return 0
        cursor.execute(f"UPDATE users SET f_name = ? WHERE username =?",(f_name.upper(),user_name,))
        connection.commit()

    elif int(update)==2 or str(update).lower()=='last name':
        l_name=input("Enter Last Name:")
        if(l_name.lower()=='exit'):
            add_cancel()
            return 0
        cursor.execute(f"UPDATE users SET l_name = ? WHERE username =?",(l_name.upper(),user_name,))
        connection.commit()

    elif int(update)==3 or str(update).lower()=='mobile number':
        number=input("Enter Contact Number:")
        if number.lower()=='exit':
            add_cancel()
            return 0
        cursor.execute(f"UPDATE users SET mob_num = ? WHERE username =?",(number,user_name,))
        connection.commit()

    elif int(update)==4 or str(update).lower()=='city':
        city=input("Enter City:")
        if city.lower()=='exit':
            add_cancel()
            return 0
        cursor.execute(f"UPDATE users SET city = ? WHERE username =?",(city.upper(),user_name,))
        connection.commit()
    opt=input(f"Do You Want To Update More Details About {user_name}?[Y/n]  ")
    if opt.lower()=='y':
            update_choice(user_name)
    return



def update_member():
    user_name=input("Enter username of member to update detail:")
    proceed=user_name_search(user_name)
    if int(proceed)==0:
        opt=input("This Username does not exist. Do You Want To Try Again?[Y/n]  ")
        if opt.lower()=='y':
            update_member()
        else:
            input("Operation: Updating Existing User Has Been Cancelled\nHit Enter To Return To Main Menu")
        return
    update_choice(user_name)
    input("Operation: Updating Details About Existing Member is Successfully Completed\nHit Enter To Return To Main Menu")
    

    

        

    

