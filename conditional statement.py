num1=100
num2=200
if(num1>num2):
    print('num1 is greater')
else:
    print('num2 is grater')
print('iam not part of if else block')

std=int(input("input enter your standard"))

if(std==1):
    print('you are in 1st standard')
elif(std==2):
    print('you are in 2nd standard')
elif(std==3):
    print('you are in 3rd standard')
else:
    print('you are in other than above standards')
#looping
start=1
end=0

while(start<end):
    print(start)
    start=start+1

for i in range(10):
    print(i)
    
for i in range(10,20):
    print(i)
    
for i in range(10,30,2):
    print(i)
for i in range (20,10,-1):
    print(i)