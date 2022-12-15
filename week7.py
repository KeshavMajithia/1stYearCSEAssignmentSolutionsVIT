#1 Write a Python Program to Find the Largest Number in a List
l=[10,2900,420,80085,45,99]
print("largest number: ",max(l))

#2 Write a Python Program to Find the Second Largest Number in a List
l=[10,2900,420,80085,45,99]
t=l
t.remove(max(t))
print("second largest number: ",max(t))

#3 Write a Python Program to Put Even and Odd elements in a List into Two Different lists
l=[69,420,80085,8008,21,100,6969,4200,69420]
even=[]
odd=[]
i=0
while(i<len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
    i=i+1
print("even list: ", even)
print("odd list: ", odd)

#4 Write a Python Program to Merge Two Lists and Sort it
l1=[69,420,80085,8008,21,100,6969,4200,69420]
l2=[10,2900,45,99]
l3=l1+l2
l3.sort()
print(l3)

#5 Write a Python Program to Sort the List According to the Second Element in Sub list
a=[['A',420],['B',80085],['C',69]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)

#6 Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort
l=[10,2900,420,80085,45,99]
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if(l[j]>l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print('Second largest number is:',l[-2])


#7 Write a Python Program to Sort a List According to the Length of the Elements
l=['lamborghini','dodge challenger','ferrari','mustang','tesla','supra']
l.sort(key=len)
print(l)

#8 Write a Python Program to Find the Union of two Lists
l1=[69,420,80085,8008,21,100,6969,4200,69420]
l2=[10,2900,45,99]
union=l1+l2
print(union)

#9 Write a Python Program to Find the Intersection of Two Lists
l1=[69,420,80085,8008,21,100,6969,4200,69420]
l2=[8754,69420,21,100,8008,123456]
t=list(set(l1) and set(l2))
print(t)

#10 Write a Python Program to print all odd indexed elements of a list
l=[320,24,4200,69420,420,80085,6625]
odd=[]
for i in range(0, len(l)):
    if i%2:
        pass
    else:
        odd.append(l[i])
print("odd indexed list: " + str(odd))
