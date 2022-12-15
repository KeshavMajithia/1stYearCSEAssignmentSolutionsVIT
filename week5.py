#1 Write a python program to print all natural numbers from 1 to n using while loop. 
n=int(input("enter the number: "))
i=0
while True:
    i=i+1
    print(i)
    if i==n:
        break 

#2 Write a python program to find sum of all odd numbers between 1 to n. 
n=int(input("enter the number: "))
x=0
for i in range(1,n+1):
    if i%2!=0:
        x=x+i
print(x)

#3 Write a python program to count number of digits in a number. 
n=int(input("enter the number: "))
x=0
while(n>0):
    n=n//10
    x=x+1
print(x)

#4 Write a python program to find first and last digit of a number.
n=int(input("enter the number: "))
f=l=n
while f>=10:
    f=f//10
print("The first digit of given number is: ",f)
while l>=10:
    l=l%10
print("The last digit of given number is: ",l)

#5 Write a python program to calculate sum of digits of a number. 
n=int(input("enter the number: "))
x=0
while(n>0):
    y=n%10
    x=x+y
    n=n//10
print(x)


#6 Write a python program to enter a number and print its reverse.
n=int(input("enter the number: "))
rev=0
while(n>0):
    x=n%10
    rev=rev*10+x
    n=n//10
print(rev)
