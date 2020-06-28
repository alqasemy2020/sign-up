name = input("Enter Your Name : ").strip().capitalize().title()
print()
age = input("Enter your age : ")
print()
gmail = input("Enter your E/Gmail : ")
print()
A =password= input("Enter your Password "" *atleast 7* : ")
#----------------------------------------------------------name-⬇
print()
name = " ".join(name.split())
key = ["~","`","!","@","#","$","%","^","&","*","(",")","-","=","[","]","{","}",";",":","\'","\"","|","\\","<",",",".",">","/","?","+"]
if key[30] in name:
    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )") 
else:
    if key[0] in name:
        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
    else:
        if key[1] in name:
            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
        else:
            if key[2] in name:
                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
            else:
                if key[3] in name:
                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                else:
                    if key[4] in name:
                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                    else:
                        if key[5] in name:
                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")

                        else:
                            if key[6] in name:
                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
    
                            else:
                                if key[7] in name:
                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
           
                                else:
                                    if key[8] in name:
                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
            
                                    else:
                                        if key[9] in name:
                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                
                                        else:
                                            if key[10] in name:
                                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                    
                                            else:
                                                if key[11] in name:
                                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                        
                                                else:
                                                    if key[12] in name:
                                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                            
                                                    else:
                                                        if key[13] in name:
                                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                
                                                        else:
                                                            if key[14] in name:
                                                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                    
                                                            else:
                                                                if key[15] in name:
                                                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                        
                                                                else:
                                                                    if key[16] in name:
                                                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                            
                                                                    else:
                                                                        if key[17] in name:
                                                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                
                                                                        else:
                                                                            if key[18] in name:
                                                                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                    
                                                                            else:
                                                                                if key[19] in name:
                                                                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                        
                                                                                else:
                                                                                    if key[20] in name:
                                                                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                            
                                                                                    else:
                                                                                        if key[21] in name:
                                                                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                
                                                                                        else:
                                                                                            if key[22] in name:
                                                                                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                    
                                                                                            else:
                                                                                                if key[23] in name:
                                                                                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                        
                                                                                                else:
                                                                                                    if key[24] in name:
                                                                                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                            
                                                                                                    else:
                                                                                                        if key[25] in name:
                                                                                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                                
                                                                                                        else:
                                                                                                            if key[26] in name:
                                                                                                                print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                                    
                                                                                                            else:
                                                                                                                if key[27] in name:
                                                                                                                    print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                                        
                                                                                                                else:
                                                                                                                    if key[28] in name:
                                                                                                                        print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                                            
                                                                                                                    else:
                                                                                                                        if key[29] in name:
                                                                                                                            print("sorry.You Only Can Write ( \"alpha\" + \"num\" , _ )")
                                                                                                
                                                                                                                        else:
                                                                                                                            print(f"Hello, {name}")
print()

b = age.isnumeric()  #----------------------------age-⬇
if b == True and int(age)<=80 :
    print(f"You Are {age}")
    print()
else:
    print("Wrong Age")
    print()

key2="@"             #---------------------------------------email-⬇
for i in gmail:
    if i ==key2:
        print("Your Gmail Is : "+gmail)
        break
else:
    print("Your Gmail Is : "+gmail+"@gmail.com")
    print()
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
    elif j == False:
        print(f"\u001b[32mAnd Your Pass** is :\u001b[37m {A.replace(A[3:-2],e)}") # Green
    else:
        print(f"\u001b[34mAnd Your Pass** is :\u001b[37m {A.replace(A[3:-2],e)}") # Blue
