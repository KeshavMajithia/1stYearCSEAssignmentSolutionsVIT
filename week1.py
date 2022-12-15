#1 Write a python program to display the current data and time.
import datetime
x=datetime.datetime.now()
print("the current date and time is: ",x)

#2 Write a python program to get the python version you are using.
import sys
x=sys.version
print("The Python version on this device is: ",x)

#3 Write a python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=int(input("Value of n: "))
print(n+(n*n)+(n*n*n))

#4 Write a python program to read and print various types of variables.
x=69
y=4.20
z="Keshav"
print(x, "has the type of ",type(x))
print(y, "has the type of ",type(y))
print(z, "has the type of ",type(z))

#5 Write a python program to print the calendar of a given month and year.
import calendar
yy=int(input("Enter Year: "))
mm=int(input("Enter Month: "))
print(calendar.month(yy, mm))
