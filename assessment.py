#sum of elements
data=[2,4,1,47,38]
res=0
for i in range(0,5):
    res=res+data[i]
print('result=',res)

data=[2,4,1,47,38]
for i in range(0,4):
    if(data[i]>data[i+1]):
       num=data[i]
print(num)       
#minimum
data=[2,4,1,47,38] 
for i in range(0,4):
      if(data[i]<data[i+1]):
         num=data[i]
print(num)    
#average of num
data=[2,4,1,47,38]
res=0
for i in range(0,5):
    res=res+data[i]
avg=res/5    
print('result=',avg)
#searching of element
data=[2,4,1,47,38]
flag=0
key=int(input("enter the element"))
for i in range(0,5):
    if(data[i]==key):
        flag=1
        break
if flag==1:
        print("element found")
else:
        print("element not found")
