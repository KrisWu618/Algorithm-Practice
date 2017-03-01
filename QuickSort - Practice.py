# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:40:54 2017

@author: kubla
"""

#https://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
def QuickSort(a):
    return(quicksorthelper(a,0,len(a) - 1))

def quicksorthelper(a,first,last):
    if first < last:
        split = partition(a, first, last)
        quicksorthelper(a,first,split - 1)
        quicksorthelper(a,split + 1, last)
    return(a)

def partition(a,first,last):
    pivot = a[first]
    left = first + 1
    right = last
    
    done = False
    while not done:
        while left <= right and a[left] <= pivot:
            left = left + 1
        while a[right] >= pivot and left <= right:
            right = right - 1
            
        if right < left:
            done = True
        else:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
            
    temp = a[first]
    a[first] = a[right]
    a[right] = temp
    return(right)

