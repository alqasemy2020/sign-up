A =password= input("Enter your Password "" *atleast 7* : ")

c=len(A)
d = c - 5
e = "*" * d
f = A.isnumeric()
h = A.isnumeric()
j = A.istitle()
if c <8:
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