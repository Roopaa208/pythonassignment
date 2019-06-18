# -*- coding: utf-8 -*-
sub1={'ravi':67,'rashmi':89,'lokesh':78}
sub2={'ravi':87,'rashmi':98,'lokesh':75}
sub3={'ravi':78,'rashmi':78,'lokesh':68}
sub4={'ravi':56,'rashmi':56,'lokesh':84}
sub5={'ravi':87,'rashmi':87,'lokesh':95}
sub6={'ravi':90,'rashmi':45,'lokesh':93}

#topper in over all subject
ravi={'sub1':67,'sub2':87,'sub3':78,'sub4':56,'sub5':87,'sub6':90}
rashmi={'sub1':89,'sub2':98,'sub3':78,'sub4':56,'sub5':87,'sub6':45}
lokesh={'sub1':78,'sub2':75,'sub3':68,'sub4':84,'sub5':95,'sub6':93}
temp=0
for i in ravi.values():
    temp=sum(ravi.values())
print(temp)
temp1=0
for i in rashmi.values():
    temp1=sum(rashmi.values())
print(temp1)    
temp2=0
for i in lokesh.values():
    temp2=sum(lokesh.values())
print(temp2)
if(temp>temp1 and temp>temp2):
    print("print ravi is topper")
elif(temp1>temp and temp1>temp2):
    print("rashmi is topper")
#elif(temp2>temp and temp2>temp1):
else:
     print("lokesh is topper")
#for highest scorer in each subjesct
if(ravi['sub1']>rashmi['sub1'] and ravi['sub1']>lokesh['sub1']):
    print('ravi is highest scorer in sub1')
elif(rashmi['sub1']>ravi['sub1'] and rashmi['sub1']>lokesh['sub1']):
    print('rashmi is highest scorer sub1')
elif(lokesh['sub1']>ravi['sub1'] and lokesh['sub1']>rashmi['sub1']):
    print('lokesh is highest scorer in sub1')
    
if(ravi['sub2']>rashmi['sub2'] and ravi['sub2']>lokesh['sub2']):
    print('ravi is highest scorer in sub2')
elif(rashmi['sub2']>ravi['sub2'] and rashmi['sub2']>lokesh['sub2']):
    print('rashmi is highest scorer in sub2')
elif(lokesh['sub2']>ravi['sub2'] and lokesh['sub2']>rashmi['sub2']):
    print('lokesh is highest scorer in sub2')  

if(ravi['sub3']>rashmi['sub3'] and ravi['sub3']>lokesh['sub3']):
    print('ravi is highest scorer in sub3')
elif(rashmi['sub3']>ravi['sub3'] and rashmi['sub3']>lokesh['sub3']):
    print('rashmi is highest scorer insub3')
elif(lokesh['sub3']>ravi['sub3'] and lokesh['sub3']>rashmi['sub3']):
    print('lokesh is highest scorer in sub3')
  
if(ravi['sub4']>rashmi['sub4'] and ravi['sub4']>lokesh['sub4']):
    print('ravi is highest scorer in sub4')
elif(rashmi['sub4']>ravi['sub4'] and rashmi['sub4']>lokesh['sub4']):
    print('rashmi is highest scorer in sub4')
elif(lokesh['sub4']>ravi['sub4'] and lokesh['sub4']>rashmi['sub4']):
    print('lokesh is highest scorer in sub4')

if(ravi['sub5']>rashmi['sub5'] and ravi['sub5']>lokesh['sub5']):
    print('ravi is highest scorer in sub5')
elif(rashmi['sub5']>ravi['sub5'] and rashmi['sub5']>lokesh['sub5']):
    print('rashmi is highest scorer in sub5')
elif(lokesh['sub5']>ravi['sub5'] and lokesh['sub5']>rashmi['sub5']):
    print('lokesh is highest scorer in sub5')
 
if(ravi['sub6']>rashmi['sub6'] and ravi['sub6']>lokesh['sub6']):
    print('ravi is highest scorer in sub6')
elif(rashmi['sub6']>ravi['sub6'] and rashmi['sub6']>lokesh['sub6']):
    print('rashmi is highest scorer in sub6')
elif(lokesh['sub6']>ravi['sub6'] and lokesh['sub6']>rashmi['sub6']):
    print('lokesh is highest scorer in sub6')
    
#using max function
sub1={'ravi':67,'rashmi':89,'lokesh':78}
sub2={'ravi':87,'rashmi':98,'lokesh':75}
sub3={'ravi':78,'rashmi':78,'lokesh':68}
sub4={'ravi':56,'rashmi':56,'lokesh':84}
sub5={'ravi':87,'rashmi':87,'lokesh':95}
sub6={'ravi':90,'rashmi':45,'lokesh':93}
print('highest is scorer in sub1',max(zip(sub1.values(),sub1.keys())))
print('highest is scorer in sub2',max(zip(sub2.values(),sub2.keys())))
print('highest is scorer in sub3',max(zip(sub3.values(),sub3.keys())))
print('highest is scorer in sub4',max(zip(sub4.values(),sub4.keys())))
print('highest is scorer in sub5',max(zip(sub5.values(),sub5.keys())))
print('highest is scorer in sub6',max(zip(sub6.values(),sub6.keys())))
# for lowest scorer
ravi={'sub1':67,'sub2':87,'sub3':78,'sub4':56,'sub5':87,'sub6':90}
rashmi={'sub1':89,'sub2':98,'sub3':78,'sub4':56,'sub5':87,'sub6':45}
lokesh={'sub1':78,'sub2':75,'sub3':68,'sub4':84,'sub5':95,'sub6':93}

temp=0
for i in ravi.values():
    temp=sum(ravi.values())
temp1=0
for i in rashmi.values():
    temp1=sum(rashmi.values())
temp2=0
for i in lokesh.values():
    temp2=sum(lokesh.values())
if(temp<temp1 and temp<temp2):
    print(" ravi is lower with score",temp)
elif(temp1<temp and temp1<temp2):
    print("rashmi is lower with scorer",temp1)
#elif(temp2<temp and temp2<temp1):
else:
    print("lokesh is lower with score",temp2)
