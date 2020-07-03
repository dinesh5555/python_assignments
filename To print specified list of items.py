#!/usr/bin/env python
# coding: utf-8

# In[2]:


Fruit = ['mango', 'apple', 'banana', 'pineapple', 'jackfruit','grapes']
Fruit = [x for (i,x) in enumerate(Fruit) if i not in (0,4,5)]
print(Fruit)

