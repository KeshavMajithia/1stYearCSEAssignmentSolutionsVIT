#1 Write a python program to check whether the given number is palindrome or not.
n=int(input("enter the number:"))
temp=n
x=0
while(n>0):
    i=n%10
    x=x*10+i
    n=n//10
if(temp==x):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#2 Write a python program to find frequency of each digit in a given integer.
x=int(input("enter the number: "))
print("Digit\tFrequency")
for i in range(0,10):
    c=0;
    temp=x;
    while temp>0:
        d=temp%10
        if d==i:
            c=c+1
        temp=temp//10;
    if c>0:
        print(i,"\t",c)

#3 Write a python program to print all ascii character with their values.
x=str(input("enter a character: "))
asc=ord(x)
print("\nASCII Value:",asc)

#4 Write a python program to find all factors of a number. 
x=int(input("enter a number: "))
f=[]
for i in range(1,x+1):
    if x%i==0:
        f.append(i)
print ("Factors of ",x, "are: ",f)

#5 Write a python program to calculate factorial of a number. 
x=int(input("enter the number: "))
f=1
if x<0:
    print("factorial of 0 doesn't exist.")
elif x==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,x + 1):
        f=f*i
    print("The factorial of ",x,"is ",f)

#6 Write a python program to print prime numbers between 1 to n. 
x=0
n=int(input("enter the number: "))
for a in range (x,n+1):
    if n>1:
        for i in range (2,a):
            if (a%i) == 0:
                break
        else:
            print(a)

#7 Write a python program to check whether a number is Armstrong, prime, strong, magic, perfect number or not.
n=int(input("enter a number to check: "))
t=m=n
u=0
if n>=0:
    if(n!=0):
        o=len(str(n))
        sum=0
    while t>0:
        d=t%10
        sum=sum+d**o
        t//=10
    if n==sum:
        u=u+1
        print(n,"is an armstrong number")
    else:
        pass
    if(n!=0):
        fl=False
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                fl=True
                break
        if fl:
            pass
        else:
            u=u+1
            print(n,"is a prime number")
    if(n!=0):
        sum=0
        t=n
        while (n):
            k=1
            f=1
            r=n % 10
            while (k<=r):
                f=f*k
                k=k+1
            sum=sum+f
            n=n//10
        if (sum==t):
            u=u+1
            print(str(t)+" is a strong number")
        else:
            pass
    if(m!=0):
        a=m
        n=0
        for i in range(1,a):
            if (a%i==0):
                n=n+i
        if (n==a):
            u=u+1
            print(str(a)," is a perfect number")
        else:
            pass
    if(m!=0):
        n=m
        c=len(str(n))
        sum=0
        t=n
        while (c>1):
            sum=0
            while (t>0):
                sum=sum+t%10
                t=t//10
            t=sum
            c=len(str(sum))
        if (sum==1):
            u=u+1
            print(m,"is a magic number")
        else:
            pass
        if u==0:
            print(n," is neither of them.")
elif n<0:
    print("the number can't be negative")

#8 Write a python program to print Fibonacci series up to n terms.
n=int(input("enter the number: "))
n1,n2=0,1
c=0
if n<=0:
    print("enter a positive integer.")
else:
    while c<n:
        print(n1)
        N=n1+n2
        n1=n2
        n2=N
        c=c+1
