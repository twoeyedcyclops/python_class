# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:21:40 2019

@author: kevin
"""

total_cost=float(input("What is the cost of your dream homes?"))
annual_salary=float(input("What is your annual salary?"))
portion_saved=float(input("What portion of your salary do you plan on saving?(decimal form)"))
portion_down_payment=total_cost*.25
current_savings=0
monthsrequired=0
while current_savings<portion_down_payment:
    monthly_salary=annual_salary/12
    r=.04
    current_savings=current_savings*r/12+monthly_salary*portion_saved+current_savings
    monthsrequired=monthsrequired+1
print("It will take ",monthsrequired," months to be able to make a down payment on your dream home")
    
    