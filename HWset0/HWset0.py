# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:35:58 2019

@author: kevin
"""
"User inputs x and y values to perform specific operations"
import math
x=input("Please Input an X-Value ")
y=input("Please Input a  Y-Value ")
x=int(x)
y=int(y)
x_y=x**y
print("x to the power of y is ", x_y)
xlog=int(math.log(x,2))
print("log base 2 of x is ", xlog)
