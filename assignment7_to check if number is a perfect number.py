#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter a number"))
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1+i
if(sum1==n):
    print("the number is a perfect number")
else:
    print("the number is not a perfect a number")

