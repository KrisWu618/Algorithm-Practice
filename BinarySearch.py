# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:12:27 2017

@author: Kris
"""
import numpy as np
def doSearch(arrays, targetValue):
    ind_min = 0
    ind_max = len(arrays) - 1
    
    check = False
    while check is not True:
        ind_temp = (ind_min + ind_max)//2
        temp = arrays[ind_temp]
        if temp < targetValue:
            ind_min = ind_temp + 1
        if temp > targetValue:
            ind_max = ind_temp - 1
        else:
            check = True
            break;
    #find the index of the target Value
    return(ind_temp)
    
target = int(input('target value:'))   
primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
result = doSearch(primes,target )
print('Found the prime at index'+ result)

# running time
import math
n = len(primes)
math.log(n) + 1