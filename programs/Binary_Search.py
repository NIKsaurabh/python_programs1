#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:17:20 2019

@author: saurabh
"""


def binary_search(a,b,mid,l,n):
    while(True):
        if(l[mid]==n):
            return n
        elif(l[mid]<n):
            a=mid+1
            mid=int((a+b)/2)
            binary_search(a,b,mid,l,n)
        elif(l[mid]>n):
            b=mid-1
            mid=int((a+b)/2)
            binary_search(a,b,mid,l,n)
        else:
            return ("Not found")
    
l=list(map(int,input().split()))
n=int(input())
mid=int((len(l)-1)/2)
print(binary_search(0,len(l)-1,mid,l,n))

