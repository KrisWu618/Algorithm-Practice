# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:53:54 2017

@author: kubla
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def pop(self):
        return(self.items.pop())
        
    def push(self,other):
        self.items.append(other)
        
    def isEmpty(self):
        return(self.items == [])
        
        
def toBinary(num):
    res = num
    s = Stack()
    while res > 1:
        res = res/2
        rem = res%2
        s.push(rem)
    
    st = ''
    while not s.isEmpty():
        st = st + str(s.pop())
        
    return(st)
    
