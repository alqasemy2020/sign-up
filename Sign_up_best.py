import shorts as sho

sho.user


sho.user_name(input("enter your name : "))


if len(sho.user) == 1:
    sho.user_age(input("enter your age : "))


if len(sho.user) == 2:
    sho.user_email(input("enter your email : "))

if len(sho.user) == 3:
    sho.user_password(input("enter your password : "))

print(sho.user)
