# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:48:32 2017

@author: kubla
"""

class queue:
    def __init__(self):
        self.items = []
    
    def isempty(self):
        return(self.items == [])
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return(self.items.pop())
    
    def size(self):
        return(len(self.items))
        

def hotpotate(namelist,num):
    q = queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(0,num):
            q.enqueue(q.dequeue())  
        q.dequeue()
    return q.dequeue()


print(hotpotate(["Bill","David","Susan"],1))