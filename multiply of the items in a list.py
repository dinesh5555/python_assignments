#!/usr/bin/env python
# coding: utf-8

# In[3]:


def multiply_list(items):
    total = 1
    for x in items:
        total *= x
    return total
print(multiply_list([4,2,3]))

