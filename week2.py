#1 Write a Python Program to Find the Square Root.
import math
x=int(input("enter the number: "))
print(math.sqrt(x))

#2 Write a Python Program to Calculate the Area and Perimeter of Triangle and Circle.
##circle
import math
radius=int(input("enter the radius of circle: "))
area=print("area of circle is: ", math.pi*radius*radius)
perimeter=print("perimeter of circle is: ", 2*math.pi*radius)
##triangle
s1 = float(input('Enter first side of triangle: '))
s2 = float(input('Enter second side of triangle: '))
s3 = float(input('Enter third side of triangle: '))
perimeter1=(s1+s2+s3) / 2
print(perimeter1)
area1=(perimeter1*(perimeter1-s1)*(perimeter1-s2)*(perimeter1-s3)) ** 0.5
print(area1)

#3 Write a Python Program to Solve Quadratic Equation.
import math
a=int(input("enter the coefficient of x^2: "))
b=int(input("enter the coefficient of x: "))
c=int(input("enter the constant term: "))
z=math.sqrt(b**2-4*a*c)
x1=(-b+z)/2*a
x2=(-b-z)/2*a
print("roots of given quadratic equation are: ",x1,",",x2)

#4 Write a Python Program to Swap Two Variables.
v1=input("Enter value of first variable: ")
v2=input("Enter value of second variable: ")
temp=v1
v1=v2
v2=temp
print("The value of first variable after swapping: ",v1)
print("The value of second variable after swapping: ",v2)

#5 Write a Python Program to Convert Kilometres to Miles.
km=float(input("enter the value in kms: "))
miles=km*0.62
print(km," kms in miles is: ",miles)

#6 Write a Python Program to Convert Celsius To Fahrenheit.
cel=float(input("enter the value in celcius: "))
far=(cel*9/5)+32
print(cel, " degrees in farenheit is: ",far)
