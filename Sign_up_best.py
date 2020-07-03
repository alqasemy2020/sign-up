user=[]


def user_name(name):
    key = ["~","`","!","@","#","$","%","^","&","*","(",")","-","=","[","]","{","}",";",":","\'","\"","|","\\","<",",",".",">","/","?","+"]
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


user_name(input("enter your name : "))


def user_age(age):

    if age.isnumeric() == False or int(age)>=90 :
        print("\u001b[31mWrong Age\u001b[0m") 
        user_age(input("enter your age again : "))
    else:
        user.append(int(age))

if len(user) == 1:
    user_age(input("enter you age : "))


def user_email(email):
    key2 = "@"
    for b in email:
        if b == key2:
            user.append(f"{email}")
            break
    else:
        user.append(f"{email}@gmail.com")

if len(user) == 2:
    user_email(input("Enter your email : "))


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


if len(user) == 3:
    user_password(input("enter your password : "))
    print(user)




