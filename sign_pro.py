name = input("Enter Your Name : ").strip().capitalize().title()
print()
age = input("Enter your age : ")
print()
gmail = input("Enter your E/Gmail : ")
print()
A =password= input("Enter your Password "" *atleast 7* : ")
#----------------------------------------------------------name-⬇
print()
name =" ".join(name.split())
print(f"Hello, {name}")
print()
#----------------------------age-⬇
b = age.isnumeric()
if b == True:
    print(f"You Are {age}")
else:
    print("Wrong Age")
print()
#---------------------------------------email-⬇
key="@"
for i in gmail:
    if i ==key:
        print("Your Gmail Is : "+gmail)
        break
else:
    print("Your Gmail Is : "+gmail+"@gmail.com")
print()
#---------------------------------------password-⬇
c=len(A)
d = c - 5
e = "*" * d
f = A.isnumeric()
j = A.istitle()
if c <7:
    print()
    print('sory, There is a problem')
    print()
else:
    if f == True:
        print(f"\u001b[31mAnd Your Pass** is :\u001b[37m {A.replace(A[3:-2],e)}") # Red
    else:
        if j == False:
          print(f"\u001b[32mAnd Your Pass** is :\u001b[37m {A.replace(A[3:-2],e)}") # Green  
        else:
            print(f"\u001b[34mAnd Your Pass** is :\u001b[37m {A.replace(A[3:-2],e)}") # Blue