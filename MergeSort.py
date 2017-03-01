# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def MergeSortArray(list_a,list_b):
    m = len(list_a)
    n = len(list_b)
    l = m+n
    list_merge = [None]*l
    
    i = 0
    j = 0
    k = 0
    while i < m and j < n:
        if list_a[i] < list_b[j]:
            list_merge[k] = list_a[i]
            i += 1
            k += 1
        else:
            list_merge[k] = list_b[j]
            j += 1
            k += 1
            
    if i < m:
        remain = list_a[i:]
    if j < n:
        remain = list_b[j:]
    
    list_merge[k:] = remain
    return(list_merge)
    
    
MergeSortArray([1,5,13],[2,9,15])
MergeSortArray([2],[1])

def MergeSort(mylist):
    if len(mylist) == 1:
        return(mylist)
    else:
        mid = len(mylist)/2
        right = MergeSort(mylist[mid:])
        left = MergeSort(mylist[:mid])
        return(MergeSortArray(left, right))
    
    
MergeSort([2,1,3,5,6])
