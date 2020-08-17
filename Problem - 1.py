#!/usr/bin/env python
# coding: utf-8

# #### Problem 1: 

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# In[1]:

sum_mul = []
sum_mul = sum([s for s in range(1000) if (s%3 and s%5)==0])
print(sum_mul)

# Answer: 233168




