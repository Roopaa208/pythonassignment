# -*- coding: utf-8 -*-
class student():
    def register(self,regno,name,standard,section):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.section=section
        
    def information(self):
        print('regno',self.regno,'name',self.name,'standard',self.standard,'section',self.section)
        
bhavikaa=student()
bhavikaa.register(101,'Bhavikaa','9','A')
bhavikaa.information()

shloka=student()
shloka.register(102,'Shloka','9','C')
shloka.information()

class calculator():
     
        
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2
       
       
calc=calculator()
result=calc.add(10,20)
print('result of additon is',result)
result1=calc.sub(10,45)
print('result of subtraction is',result1)
result2=calc.mul(13,9)
print('result of multiplication is',result2)
result3=calc.div(30,5)
print('result of division is',result3)

