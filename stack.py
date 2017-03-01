# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:46:22 2017

@author: kubla
"""

class stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return(self.items == [])
    
    def push(self,other):
        return(self.items.append(other))
    
    def pop(self):
        return(self.items.pop())
        
    def peek(self):
        return(self.items[len(self.items) - 1])
        
    def size(self):
        return(len(self.items))
    
    
s=stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
