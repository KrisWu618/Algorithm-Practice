#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:36:46 2017

@author: kubla
"""

class Complexy3:

    def __init__(self,num1,num2):

        self.real = num1
        self.imag = num2
        
    def __str__(self):
    
        return(str(self.real) + '+'+ str(self.imag)+'i')
        
    def __add__(self,other):
        add_real = self.real + other.real
        add_imag = self.imag + other.imag
        return(Complexy3(add_real,add_imag))
    
    def __mul__(self,other):
        mp_real = self.real*other.real
        mp_imag = self.imag*other.imag
        return(Complexy3(mp_real,mp_imag))
    
    def __eq__(self,other):
        return(self.real == other.real and self.imag == other.imag)
        

c1 = Complexy3(3,5)
c2 = Complexy3(2,2)
c3=c1+c2
c4=c1*c2
      
class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
        
        
f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        