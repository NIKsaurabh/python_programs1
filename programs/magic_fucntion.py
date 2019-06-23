#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:18:14 2019

@author: saurabh
"""

class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        tempN=self.num*other.den+self.den*other.num
        tempD=self.den*other.den
        return Fraction(tempN,tempD)
    def __sub__(self,other):
        tempN=self.num*other.den-self.den*other.num
        tempD=self.den*other.den
        return Fraction(tempN,tempD)
    def __mul__(self,other):
        tempN=self.num*other.num
        tempD=self.den*other.den
        return Fraction(tempN,tempD)
    def __truediv__(self,other):
        tempN=self.num*other.den
        tempD=self.den*other.num
        return Fraction(tempN,tempD)