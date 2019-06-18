class class1():
    def method1(self):
        print('class1:method 1')
    def method2(self):
        print('class2:method 2')
        
        
class class2():
    def method3(self):
        print('class2:method 3')
    def method4(self):
        print('class2:method 4')
# -*- coding: utf-8 -*-

print(__name__)
def main1():
    print('hello world')
    otherfunction()
def otherfunction():
    print('this is another function')
    
if (__name__=='__main__'):
    main1()
