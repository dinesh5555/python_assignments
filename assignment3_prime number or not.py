#!/usr/bin/env python
# coding: utf-8

# In[19]:


num=int(input("enter a number"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
         print(num,"is not a prime number")
         break
    else:
     print(num,"is a prime number")

