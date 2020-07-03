#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the value of n"))
f=0
s=1
i=0
while(i<n):
    next=f+s
    f=s
    s=next
    i=i+1
    print(next)

