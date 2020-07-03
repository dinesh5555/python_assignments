#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(6))

