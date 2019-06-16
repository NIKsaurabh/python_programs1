#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:37:45 2019

@author: saurabh
"""
#only for 2D list
l1=[1,2,3,[4,5]]
l2=[]
for i in range(len(l1)):
    if type(l1[i]) is list:
        l2.extend(l1[i])
    else:
        l2.append(l1[i])
print(l2)