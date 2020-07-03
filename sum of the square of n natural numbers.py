#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input("enter the number"))
def sqsum(n) :
   sum = 0
   for i in range(1, n+1) :
      sum = sum + pow(i,2)
   return sum
print(sqsum(n))

