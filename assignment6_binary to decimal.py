#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=list(input("input a binary number:"))
value=0
for i in range(len(num)):
    digit=num.pop()
    if digit=='1':
        value=value+pow(2,i)
        print("the decimal value of he number is",value)

