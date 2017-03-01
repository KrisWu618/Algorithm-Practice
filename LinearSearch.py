# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:45:45 2017

@author: kubla
"""

def LinearSearch(myArray, value):
    found = False
    i = 0
    while not found and i < len(myArray):
        if myArray[i] != value:
            i += 1
        else:
            found = True
            break
    if not found:
        print('Sorry')
    else:
        print('Your element is at the position:'+ str(i))