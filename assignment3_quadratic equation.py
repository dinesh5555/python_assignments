#!/usr/bin/env python
# coding: utf-8

# In[81]:


import math
print("quadratic function:(a*x^2)+b*x+c")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
r=(b*b)-(4*a*c)
if(r>0):
 x1=(-b+math.sqrt(r)/(2*a))
 x2=(-b-math.sqrt(r)/(2*a))
 print("there are two roots: %f and %f"%(x1,x2))
elif(r==0):
     x1=x2=-b/(2*a)
     print("there is one root:",x1,x2)
else:
  print("no roots,discriminant<0.")


# In[ ]:




