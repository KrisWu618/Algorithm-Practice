# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:30:22 2017

@author: kubla
"""
def QuickSort(mylist,start,end):
    if start < end:
        pivot = PartitionArray(mylist, start, end)
        QuickSort(mylist,pivot + 1, end)
        QuickSort(mylist,start,pivot - 1)    
    return(mylist)
    
    



def PartitionArray(mylist,start,end):  
    pivot = mylist[end]
    left = start 
    #right = end - 1
    if left < end:
        i = left
        while i < end:
            if mylist[i] < pivot:
                temp = mylist[left]
                mylist[left] = mylist[i]
                mylist[i] = temp
                left += 1
            i += 1
    
    temp = mylist[left]
    mylist[left] = mylist[end]
    mylist[end] = temp
    pivotLoc = left
    return(pivotLoc)



a = [9,4,8,1,4,5,6]
QuickSort(a,0,6)
            
