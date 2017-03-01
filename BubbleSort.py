# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:48:11 2017

@author: kubla
"""

def BubbleSort(a):
    temp = 0
    n = len(a)
    for i in range(1,n): # pass
        for j in range(0,(n-i)): # cmoparison
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return(a)
    
