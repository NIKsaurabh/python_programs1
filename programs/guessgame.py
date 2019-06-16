#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:01:23 2019

@author: saurabh
"""
import random
cond=True
count=0
t=(random.randint(1,100))
while(cond): 
    user=int(input("Enter number : "))
    if t>user:
        print("enter greater number")
        count+=1
    elif t<user:
        print("enter less number")
        count+=1
    else:
        print("Congratulations!!!!!!!")
        count+=1
        print("You guessed in",count,"times")
        cond=False
        

    
