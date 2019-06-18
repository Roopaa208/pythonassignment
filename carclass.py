# -*- coding: utf-8 -*-

class car():
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        self.speed=0
        
    def start(self):
        self.speed=0
        return self.speed
    def move(self):
        self.speed=self.speed+5
        return self.speed
    def stop(self):
        self.speed=0
        return self.speed
    def info(self):
        print('make',self.make,'model',self.model,'color',self.color,'price',self.price,'speed',self.speed)
        
mycar=car('shift','nano','yellow',1200000)
mycar.info()
print('car in move',mycar.move())
print('car in start',mycar.start())
print('car in stop',mycar.stop())


        
        
