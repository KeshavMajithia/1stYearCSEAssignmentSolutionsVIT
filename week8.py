#1 Write a Python program to get the 4th element and 4th element from last of a tuple.
x=(69,420,80085,8008,69420,21,88,6699,99,66)
print('fourth number: ', x[3],'\nlast 4th number: ', x[-4])

#2 Write a Python program to find the repeated items of a tuple. 
x=(69,420,80085,8008,69420,21,88,6699,99,66,69420,80085,8008)
for i in x:
    if x.count(i)>1:
        print(i)

#3 Write a Python program to check whether an element exists with a tuple. 
x=(69,420,80085,8008,69420,21,88,6699,99,66,69420,80085,8008)
a=int(input("enter the number to check: "))
if a in x:
    print("True")
else:
    print("False")

#4 Write a Python program to unzip a list of tuples into individual lists. 
x=[(69,420,80085),(8008,69420),(21,88),(6699,99),(66,69420),(80085,8008)]
a=list(zip(*x))
print(a)

#5 Write a Python program to replace last value of tuples in a list.
x=[(10,20,40),(40,50,60),(70,80,90)]
print([t[:-1]+(100,) for t in x])

#6 Write a Python program to remove an empty tuple(s) from a list of tuples. 
x=[(),(69,420,80085),(21,88),(),(6699,99),(66,69420),(),(80085,8008)]
x=[t for t in x if t]
print(x)

#7 Write a Python program to convert a list of tuples into a dictionary. 
x=[('abc',1),('def',2),('ghi',3),('jkl',4),('mno',5)]
a=dict(x)
print(a)

#8 Write a Python program to find the highest 3 values of corresponding keys in a dictionary
from collections import Counter as c
x={'t': 420, 'u': 69, 't': 8008, 'o': 69420, 'r': 80085}
a=c(x)
h=a.most_common(5)
for i in h:
    print(i[0]," :",i[1])
