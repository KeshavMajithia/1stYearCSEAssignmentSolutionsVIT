#1 Write a Python program to find those numbers which are divisible by 7 and not a multiple of 5, between 2000 and 3200both included). 
x=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        x.append(int(i))
print (x,",") 

#2 Write a python program to check whether a number is divisible by 5 and 11 or not. 
x=int(input("enter the number: "))
if (x%5==0) and (x%11==0):
    print("the given number is divisible by 5 and 11.")
else:
    print("the given number is not divisible by 5 and 11.")

#3 Write a python program to check whether a character is alphabet or not. 
x="Keshav"
y="5911"
if (x.isalpha()==True):
    print(x,"contains alphabets.")
else:
    print(x,"doesn't contain alphabets.")
if (y.isalpha()==True):
    print(y,"contains alphabets.")
else:
    print(y,"doesn't contain alphabets.")

#4 Write a python program to input any character and check whether it is alphabet, digit or special character. 
x=input("input here: ")
if (x.isalpha()==True):
    print(x,"is alphabet")
elif(x>='0' and x<='9'):
    print(x, "is a digit")
else:
    print(x, "is a special character")

#5 Write a python program to check whether a character is uppercase or lowercase. 
x= input("enter here: ")
if(x.isupper()):
    print(x,"is in UPPERCASE")
elif(x.islower()):
    print(x,"is in lowercase")
else:
    print(x, "is in both UPPERCASE and lowercase")

#6 Write a python program to input week number and print weekday.
x= int(input("enter week day: "))
if(x==1):
    print("Sunda");
elif(x==2):
    print("Monday")
elif(x==3):
    print("Tuesday")
elif(x==4):
    print("Wednesday")
elif(x==5):
    print("Thursday")
elif(x==6):
    print("Friday")
elif(x==7):
    print("Saturday")
else:
    print("invalid weekday")

#7 Write a python program to count total number of notes in a given amount. 
x=[2000,500,200,100,50,10,5,1]
y=int(input("enter the value: "))
i=0
total=y
while y>0:
    if y>x[i]:
        count=y//x[i]
        print(count,"notes of",x[i])
    y=y%x[i]
    i=i+1
print("total amount:",total) 
