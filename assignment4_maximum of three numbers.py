#!/usr/bin/env python
# coding: utf-8

# In[8]:


def maximum(a,b,c):
    if(a>=b)and(a>=c):
        print("maximum is",a)
    elif(b>=a)and(b>=c):
            print("maximum is",b)
    else:
            print("maximum is",c)
    return maximum
maximum(30,20,10)

