#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check(string,sub_str):
    if (string.find(sub_str)== -1):
        print("no")
    else:
        print("yes")
string="harry potter"
sub_str="harry"
check(string, sub_str)

