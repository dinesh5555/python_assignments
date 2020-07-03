#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
    print("the no of digits in the number:",count)

