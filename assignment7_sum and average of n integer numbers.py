#!/usr/bin/env python
# coding: utf-8

# In[2]:


count=0
sum=0.0
number=1
while number!=0:
    number=int(input(""))
    sum=sum+number
    count +=1
if count==0:
    print("input some numbers")
else:
    print("average and sum of the above numbers are:",sum/(count-1),sum)

