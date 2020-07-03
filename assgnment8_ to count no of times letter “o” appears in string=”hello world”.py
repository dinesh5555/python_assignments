#!/usr/bin/env python
# coding: utf-8

# In[5]:


string="hello world"
char=input("enter the character:")
count=0
for i in string:
    if(i==char):
        count=count+1
print("no of times 0 appears in given string is",count)

