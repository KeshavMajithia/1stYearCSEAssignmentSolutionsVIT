#Write a Python function that prints out the first n rows of Pascal's triangle.
def pt(n):
   tr=[1]
   y=[0]
   for x in range(max(n,0)):
      print(tr)
      tr=[l+r for l,r in zip(tr+y,y+tr)]
   return n>=1
n=int(input("enter the number of rows: "))
pt(n)

#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def sq():
	l=list()
	for i in range(1,31):
		l.append(i**2)
	print(l)
sq()

#Write a Python program to detect the number of local variables declared in a function.
def detect():
    x=6
    y=9
    z=69.420
    a="KM"
    b="80085"
    print("Hello World")
print(detect.__code__.co_nlocals)

#Write a Python program that invoke a given function after specific milliseconds.
from time import sleep
import math
def delay(fn,ms,*args):
  sleep(ms/1000)
  return fn(*args)
print("Square root after specific miliseconds:") 
print(delay(lambda x:math.sqrt(x),100,16))
print(delay(lambda x:math.sqrt(x),1000,100))
print(delay(lambda x:math.sqrt(x),2000,25100))

#Write a Python program to get the sum of a non-negative integer.
def s(n):
  if n==0:
    return 0
  else:
    return n%10+s(int(n/10))
print(s(69))
print(s(420))
