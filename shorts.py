user = []

import re

def user_name(name):
    key = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "[", "]", "{", "}", ";", ":", "\'", "\"", "|", "\\", "<", ",", ".", ">", "/", "?", "+"]
    a = 0
    while a < len(key) :  # 31
        if key[a] in name:
            print("\u001b[31msorry.You Only Can Write ( \"alpha\" + \"num\" , _ )\u001b[0m")
            user_name(input("enter your name again : "))
            break
        a +=1
    else:
        name.strip().capitalize()
        name=" ".join(name.split())
        user.append(name)       


def user_age(age):

    if age.isnumeric() == False or int(age)>=90 :
        print("\u001b[31mWrong Age\u001b[0m") 
        user_age(input("enter your age again : "))
    
    else:
        return user.append(age)


def user_email():
    btw = 20
    while btw > 0:
        try:
            email = input("enter your email : ")
            my_re = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|edu|co|ru|sa|uk)$",email)
            chk_email =  re.search(r"^[A-z0-9\.]+",email)
            chk = len(chk_email.group())
            if chk > 30:
                print("The Email Should Be Between 6 and 30 characters")
                btw -= 1
                a
            else:
                user.append(my_re.group())
            break
        except:
            print("wrong email")
            btw -= 1
    else:
        print("Are You Kidding With Me ?!")




def user_password(passwordd):
    global password

    password = passwordd

    c=len(password)
    d = c - 4
    e = "*" * d
    f = password.isnumeric()
    j = password.istitle()
    if c <7:
        print()   
        print('at least 7 letters')
        user_password(input("Enter your password again correctly : "))
    else:
        def if_pass(password2):   
            password2 = password2.strip().capitalize()
                # Updatting Option
            if password2 == "Update":
                print()
                user_password(input("Enter the new password \'\u001b[30;1madd some letter\u001b[0m\' : "))
                # Keepping Option
            elif password2 == "Keep":
                user.append(f"{passwordd}")
            else:
                print("\u001b[31mworng option choosed\u001b[0m")
                if_pass(input("\u001b[30;1mYour password is very weak \u001b[0m keep or update \u001b[30;1mThe password\u001b[0m: "))       
    
        if f == True:
            print(f"\u001b[31mYour Pass** is :\u001b[0m {password.replace(password[3:-2],e)}") # Red
            print()
            if_pass(input("\u001b[30;1mYour password is very weak \u001b[0m keep or update \u001b[30;1mThe password\u001b[0m: "))

        elif j == False:
            user.append(f" {password.replace(password[3:-2],e)} ") # Green
        else:
            user.append(f" {password.replace(password[3:-2],e)} ") # Blue
