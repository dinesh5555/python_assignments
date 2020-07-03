#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("enter a number:"))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()

