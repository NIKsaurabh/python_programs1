#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 08:57:40 2019

@author: saurabh
"""
import sys
l=list(map(int,input().split(",")))
#for month
if 1 in l:
    l.pop(l.index(1))
    if 2 in l:
        l.pop(l.index(2))
        mm=12

    elif 1 in l:
        l.pop(l.index(1))
        mm=11
        
    elif 0 in l:
        l.pop(l.index(0))
        mm=10

elif 0 in l:
    l.pop(l.index(0))
    mm=str(0)+str(max(l))
    l.pop(l.index(max(l)))
    if mm==00:
        print(0)
        sys.exit(0)
else:
    print(0)
    sys.exit(0)

#for date
if int(mm) in (1,3,5,7,8,10,12):
    if 3 in l:
        l.pop(l.index(3))
        if 1 in l:
            l.pop(l.index(1))
            dd=str(3)+str(1)
        elif 0 in l:
            l.pop(l.index(0))
            dd=str(3)+str(0)
    elif 2 in l:
        l.pop(l.index(2))
        dd=str(2)+str(max(l))
        l.pop(l.index(max(l)))
    elif 1 in l:
        l.pop(l.index(1))
        dd=str(1)+str(max(l))
        l.pop(l.index(max(l)))
    elif 0 in l:
        l.pop(l.index(0))
        if max(l)==0:
            print(0)
            sys.exit(0)
        else:
            dd=str(0)+str(max(l))
            l.pop(l.index(max(l)))
    else:
        print(0)
        sys.exit(0)
elif int(mm) in (4,6,9,11):
    if 3 in l:
        l.pop(l.index(3))
        if 0 in l:
            l.pop(l.index(0))
            dd=str(3)+str(0)
    elif 2 in l:
        l.pop(l.index(2))
        dd=str(2)+str(max(l))
        l.pop(l.index(max(l)))
    elif 1 in l:
        l.pop(l.index(1))
        dd=str(1)+str(max(l))
        l.pop(l.index(max(l)))
    elif 0 in l:
        l.pop(l.index(0))
        dd=str(0)+str(max(l))
        l.pop(l.index(max(l)))
    else:
        print(0)
        sys.exit(0)
elif int(mm) in (2):
    l.pop(l.index(2))
    if 2 in l:
        l.pop(l.index(2))
        if 8 in l:
            l.pop(l.index(8))
            dd=str(2)+str(8)
        elif 7 in l:
            l.pop(l.index(7))
            dd=str(2)+str(7)
        elif 6 in l:
            l.pop(l.index(6))
            dd=str(2)+str(6)
        elif 5 in l:
            l.pop(l.index(5))
            dd=str(2)+str(5)
        elif 4 in l:
            l.pop(l.index(4))
            dd=str(2)+str(4)
        elif 3 in l:
            l.pop(l.index(3))
            dd=str(2)+str(3)
        elif 2 in l:
            l.pop(l.index(2))
            dd=str(2)+str(2)
        elif 1 in l:
            l.pop(l.index(1))
            dd=str(2)+str(1)
        elif 0 in l:
            l.pop(l.index(0))
            dd=str(2)+str(0)
    elif 1 in l:
        l.pop(l.index(1))
        dd=str(1)+str(max(l))
        l.pop(l.index(max(l)))
    elif 0 in l:
        l.pop(l.index(0))
        if max(l)==0:
            print(0)
            sys.exit(0)
        else:
            dd=str(0)+str(max(l))
            l.pop(l.index(max(l)))
    else:
        print(0)
        sys.exit(0)
else:
    
    print(0)
    sys.exit(0)

#for hour
if 2 in l:
    l.pop(l.index(2))
    if 3 in l:
        l.pop(l.index(3))
        hh=str(2)+str(3)
    elif 2 in l:
        l.pop(l.index(2))
        hh=str(2)+str(2)
    elif 1 in l:
        l.pop(l.index(1))
        hh=str(2)+str(1)
    elif 0 in l:
        l.pop(l.index(0))
        hh=str(2)+str(0)
elif 1 in l:
    l.pop(l.index(1))
    hh=str(1)+str(max(l))
    l.pop(l.index(max(l)))
elif 0 in l:
    l.pop(l.index(0))
    hh=str(0)+str(max(l))
    l.pop(l.index(max(l)))
else:
    print(0)
    sys.exit(0)
#for minutes
if 5 in l:
    l.pop(l.index(5))
    MM=str(5)+str(max(l))
    l.pop(l.index(max(l)))
elif 4 in l:
    l.pop(l.index(4))
    MM=str(4)+str(max(l))
    l.pop(l.index(max(l)))
elif 3 in l:
    l.pop(l.index(3))
    MM=str(3)+str(max(l))
    l.pop(l.index(max(l)))
elif 2 in l:
    l.pop(l.index(2))
    MM=str(2)+str(max(l))
    l.pop(l.index(max(l)))
elif 1 in l:
    l.pop(l.index(1))
    MM=str(1)+str(max(l))
    l.pop(l.index(max(l)))
elif 0 in l:
    l.pop(l.index(0))
    MM=str(0)+str(max(l))
    l.pop(l.index(max(l)))
else:
    print(0)
    sys.exit(0)

print(str(mm)+"/"+str(dd)+" "+str(hh)+":"+str(MM))    
    