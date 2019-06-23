#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:02:23 2019

@author: saurabh
"""

def pali(string):
    if(len(string)<=1):
        print("Palindrome")
    else:
        if string[0]==string[-1]:
            pali(string[1:-1])
            
        else:
            print("not palindrome")
pali("malayalam")