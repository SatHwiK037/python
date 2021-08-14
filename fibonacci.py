n=int(input("enter the number of terms to be displayed"))
a=0
b=1
i=0
if n<=0:
    print("pls enter positive number")
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    while i<=n:
       print(a) 
       t=a+b
       a=b
       b=t
       i+=1
