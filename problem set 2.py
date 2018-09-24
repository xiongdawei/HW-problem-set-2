#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
problem set 2

@author: davidxiong
"""

#problem 1
def remainingbalance(balance,annual_interest,payment_rate,month):
    mir=annual_interest/12
    ubem = balance*((1-payment_rate)**month)*((1+mir)**month)
    return round(ubem,2)
 
    
print(remainingbalance(5000,0.18,0.71,11))



# probelm 2
def lowest(balance,annual_interest):
    init_balance=balance
    rate= annual_interest/12
    payment=0
    while balance>0:
        for i in range(12):
            balance = (balance-payment)*(1+rate)
        if balance>0:
            payment+=0.5
            balance=init_balance
        elif balance<=0:
                break
    return('lowest payment:',payment)
        
    
def bis(balance,annual_interest):
    rate = annual_interest/12
    mplb = balance/12 #montly payment lower bound
    mpub = (balance*(1+rate)**12)/12 #montly payment upper bound
    
# problem 3
    while True:
         mid = (mplb+mpub)/2
         unpaid=balance
         for i in range(12):
             unpaid=(unpaid-mid)*(1+rate)
         if abs(unpaid)<0.001:
            return round(mid,2)
         elif unpaid>0.001:
         	mplb=mid
         elif unpaid< -0.001
            mpub=mid





        