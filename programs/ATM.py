#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:15:10 2019

@author: saurabh
"""

class Atm:
    pin=""
    balance=0
    counter=1000
    custId=""
    
    def __init__(self):
        print("Hi, customer. Good morning")
        self.pin=input("Enter a 4 digit no to create your pin")
        print("lkdsjlkdsj")
        self.custId=self.counter+1
        Atm.counter=Atm.counter+1
        print("your custId is",self.custId)
        
    def checkBalance(self):
        user_pin=input("Enter your pin to proceed")
        if user_pin==self.pin:
            print("Your current balabce is",self.balance)
        else:
            print("Dusre ka balance jan k kya karoge?")
    def deposit(self):
        user_pin=input("Enter your pin to proceed")
        if user_pin==self.pin:
            deposit=int(input("Enter the amount to be deposited"))
            self.balance=self.balance+deposit
            print("Deposit Successful")
        else:
            print("Jayada h kya, mujhe dede")
    def withdraw(self):
        user_pin=input("Enter your pin to proceed")
        if user_pin==self.pin:
            amount=int(input("Enter the amount to be withdrawn"))
            if self.balance>amount:
                self.balance=self.balance-amount
                print("Mil gye n?")
            else:
                print("Sale Garib!")
        else:
            print("Sale Chor!!!!")
            
    def changePin(self):
        user_pin=input("Enter your pin to proceed")
        if user_pin==self.pin:
            new_pin=input("Enter Your new pin")
            if new_pin!=self.pin:
                self.pin=new_pin
                print("Your pin has been updated")
            else:
                print("mazak chal rha h kya?")
        else:
            print("Bhullakad!!!")
    