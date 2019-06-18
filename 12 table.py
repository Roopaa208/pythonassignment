# -*- coding: utf-8 -*-
n1=int(input('enter the number'))

for i in range(10,0,-1):
    a=n1*i
    print(n1,"*",i,"=",a)
#simple interest
p=int(input('enter the price'))
t=int(input('enter the time'))
r=int(input('enter the rate'))
def simple(p,t,r):
    SI=(p*t*r)/100
    return SI
    
result=simple(p,r,t)
print('SI=',result)
#prime numbers
num1 = int(input("Enter lower range: "))  
num2 = int(input("Enter upper range: "))  
  
for i in range(num1,num2 + 1):  
   if i > 1:  
       for n in range(2,i):  
           if (i % n) == 0:  
               break  
       else:  
           print(i)  
#fibbonaic series
nterms = 10
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
       #other method
def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
#electric bill
num=int(input('enter the input'))
if num<=100:
    print('rate per rupees is 2=',num*2)
elif num>100 and num<=200:
    print('rate per rupees is 3=',num*3)
elif num>200 and num<=300:
    print('rate per rupees is 5=',num*5)
else:
    print('rate per rupees is 6=',num*6)
