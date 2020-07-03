#!/usr/bin/env python
# coding: utf-8

# In[3]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("maximum element in the list is :", max(lst), "\n minimum element in the list is :", min(lst))

