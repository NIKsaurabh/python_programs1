#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:02:36 2019

@author: saurabh
"""
# only for 2d list
l1=[1,2,3,[4,5]]
l2=[]
for i in range(len(l1)):
    if type(l1[i]) is list:
        for j in range(len(l1[i])):
            l2.append(l1[i][j])
    else:
        l2.append(l1[i])
print(l2)