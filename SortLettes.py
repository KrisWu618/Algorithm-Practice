# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:00:05 2017

@author: kubla
"""

import re
def  sortSegments(s):
    string_list = re.split(r'(\d+)',s)
    for i in range(0,len(string_list)):
        string_list[i] = ''.join(sorted(string_list[i]))
    merge = ''.join(string_list)
    return(merge)
    
