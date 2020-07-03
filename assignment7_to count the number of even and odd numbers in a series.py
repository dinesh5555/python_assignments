#!/usr/bin/env python
# coding: utf-8

# In[13]:


list1 =[10,25,30,64,7,6,1]
even_count=0
odd_count= 0
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even numbers in the list:",even_count)
print("odd numbers in the list:",odd_count)

