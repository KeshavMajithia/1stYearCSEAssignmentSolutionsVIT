#1 Write a Python program to find whether the given number is Even or Odd using ternary operator.
x=int(input("enter the number: "))
if (x%2)==0:
    print(x," is an even number.")
else:
    print(x," is an odd number.")

#2 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
x=int(input("enter the number: "))
diff=x-17
if x>17:
    y=diff*2
    print(y)
else:
    print(diff)

#3 Write a Python program to test whether a number is within 100 of 1000 or 2000.
n=int(input("enter the number: "))
if (abs(n-1000))<=100 or (abs(n-2000))<=100:
    print(n,"is within 100 of 1000 or 2000")
else:
    print(n,"is not within 100 of 1000 or 2000")

#4 Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
z=int(input("enter the third number: "))
if x==y==z:
    print("the output of given equal numbers is:",x*y*z)
else:
    print("the output of given unequal numbers is:",x+y+z)

#5 Write a Python Program to Find the Factorial of a Number
x=int(input("enter the number: "))
f=1
if x<0:
    print("factorial of negative numbers doesn't exist.")
elif x==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,x+1):
        f=f*i
    print("factorial of",x,"is",f)

#6 Write a Python Program to print maximum of 3 numbers
x=float(input("enter the first number: "))
y=float(input("enter the second number: "))
z=float(input("enter the third number: "))
if (x>=y) and (x>=z):
    max=x
elif (y>=x) and (y>=z):
    max=y
else:
    max=z
print("The maximum number is:",max)

#7 Write a python program to find whether a given year is leap or not.
year=int(input("enter the year: "))
if (year%400==0) and (year%100==0):
    print(year, "is a leap year")
elif (year%4==0) and (year%100!=0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
