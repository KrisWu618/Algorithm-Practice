# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:35:06 2017

@author: kubla
"""

def InsertionSort(a):
    n = len(a)
    temp = 0
    for k in range(1,n):
        temp = a[k]
        j = k - 1
        while temp < a[j] and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return(a)
                
a = [5,4,3,2,1]
InsertionSort(a)