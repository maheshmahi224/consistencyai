import random

options=("r","p","s")

comp_choice=random.choice(options)

user_choice=input("choose the option (r\p\s) : ").lower()

if user_choice="y" and :
    print(f"your choice : {user_choice}")
    print(f"computer choice : {comp_choice}")
    print("TRY AGAIN")

elif user_choice!=comp_choice:
    print(f"your choice : {user_choice}")
    print(f"computer choice : {comp_choice}")
    print("YOU LOST BETTER LUCK NEXT TIME")
else:
    print("INVAILD SELECTION")