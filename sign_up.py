name = input("Enter Your Name : ").strip().capitalize().title()
print()
name = " ".join(name.split())
key = ["~","`","!","@","#","$","%","^","&","*","(",")","-","=","[","]","{","}",";",":","\'","\"","|","\\","<",",",".",">","/","?","+"]

t = 0

while t < len(key) :  # 31
    if key[t] in name:

        print("\u001b[31msorry.You Only Can Write ( \"alpha\" + \"num\" , _ )\u001b[0m")
        break
    t +=1 
else:
    age = input("Enter your age : ")
    b = age.isnumeric()  #----------------------------age-⬇
    if b == False or int(age)>=80 :
        print("\u001b[31mWrong Age\u001b[0m")
    else:
        gmail = input("Enter your E/Gmail : ")
        print()
        A =password= input("Enter your Password "" *atleast 7* : ")
        c=len(A)
        d = c - 5
        e = "*" * d
        f = A.isnumeric()
        j = A.istitle()
        if c <7:
            print()   
            print('\u001b[31mat least 7 letters\u001b[0m')
            A =password= input("Enter your Password "" *atleast 7* : ")
            print()
        else:
            print()
            print(f"Hello, {name}")
            print()
            print(f"You Are {age}")
            print()
            key2="@"           #---------------------------------------email-⬇
            for i in gmail:
                if i ==key2:
                    print("Your Gmail Is : "+gmail)
                    break
            else:
                print("Your Gmail Is : "+gmail+"@gmail.com")
                print()
                if f == True:
                    print(f"\u001b[31mAnd Your Pass** is :\u001b[0m {A.replace(A[3:-2],e)}") # Red
                    Change_Pass = input("\u001b[30;1mYour password is very weak \u001b[0m keep or update \u001b[30;1mThe password\u001b[0m: ").strip().capitalize()
                                                                                                                                           
                    # Updating Option
                    if Change_Pass=="Update":
                        TheNewPassword = input("Enter the new password \'add some letter\' : ")
                        A = TheNewPassword
                        cU=len(A)
                        dU = cU - 5
                        eU = "*" * dU
                        fU = A.isnumeric()
                        jU = A.istitle()
                        if jU == False:
                            print(f"\u001b[32mYour New Pass*** is :\u001b[0m {A.replace(A[3:-2],eU)}") # Green
                        else:
                            print(f"\u001b[34mYour New Pass*** is :\u001b[0m {A.replace(A[3:-2],eU)}") # Blue
                            # Keeping Option
                    elif Change_Pass=="Keep":
                        print(f"\u001b[30mAnd Your Pass*** is :\u001b[0m {A.replace(A[3:-2],e)}")
                        # Wrong Option
                    else:
                        print("\u001b[30mworng option choosed\u001b[0m")

                elif j == False:
                    print(f"\u001b[32mAnd Your Pass*** is :\u001b[0m {A.replace(A[3:-2],e)}") # Green
                else:
                    print(f"\u001b[34mAnd Your Pass*** is :\u001b[0m {A.replace(A[3:-2],e)}") # Blue
