# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:10:16 2019

@author: kevin
"""
starting_a_salary=float(input("What is your staring salary? "))
starting_msalary=starting_a_salary/12
semi_annual_raise=.07
r=.04
down_paymentpercent=.25
housecost=1000000
down_payment=down_paymentpercent*housecost
upper=10000
lower=0
steps=0
while abs(upper-lower)>=5: #'runs until difference between lower and upper limits is less than 10'
    guess=int((upper+lower)/2) # 'guess is =5000 (50%)'
    current_savings=0          # 'saving = 0'
    m_salary=starting_msalary  # 'salary = starting salary
    for month_current in range(1, 37):
        current_savings=current_savings*r/12+m_salary*guess/10000+current_savings #'run for 36 months to 
        if month_current%6==0:
            m_salary=m_salary*(1+semi_annual_raise) #'increase salary every 6 months
    if down_payment<current_savings: #'if down payment is less than current savings then choose lower portion by setting lower limit = guess
        upper=guess
    if down_payment>current_savings:
        lower=guess
    if lower>9990:
        print('You can not make enough for the down payment in 3 years')
        break
    steps=steps+1 #'step track
   #'measure difference
print(guess/10000)
print(steps)