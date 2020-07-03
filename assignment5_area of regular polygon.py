#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import tan,pi
n_sides=int(input("input no of sides:"))
s_length=float(input("input the length of a side:"))
p_area=n_sides*(s_length**2)/(4*tan(pi/n_sides))
print("the area of polygion is:",p_area)

