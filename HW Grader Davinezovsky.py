#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 09:01:44 2018
n: the number of sides
s: the length of each sides
return the perimeter of the polygon

@author: davidxiong
"""
import math
def polysum(n,s):
    perimeter = n*s
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    return perimeter**2 + area



    
    
    

