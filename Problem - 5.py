#!/usr/bin/env python
# coding: utf-8

def lowest_multiple():
    end = 20
    n1 = 11
    n2 = n1 + 1
    number = 0
    while n2 <= end:
        n1 = lcm(n1,n2)
        n2 += 1
    print(n1)

def lcm(n1,n2):
    if n1 > n2:
        large = n1
    else:
        large = n2
    while True:
        if (large % n2 == 0) and (large % n1 == 0):
            lcm = large
            break
        else:
            large += 1    
    return lcm   

lowest_multiple()

# 232792560


