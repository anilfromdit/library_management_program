from os import system
from account import create_new_account, login
from db_init import *
cursor.execute("SELECT * FROM Accounts")
new = cursor.fetchall()
if len(new) == 0:
    system("cls")
    print("****** Welcome To Library Management Program ******")
    print("\nIt Seems Like You're Using This Program For First Time\nLet's Get Started By Creating An Account First")
    done=create_new_account()
    if done != 1:
        exit()

while(1):
    system("cls")
    login()