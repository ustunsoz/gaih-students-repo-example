#!/usr/bin/env python
# coding: utf-8

# In[13]:


mylist1 = [51,53,55,57,59]
mylist2 = [52,54,56,58,60]
mylist = mylist1 + mylist2
mylist.sort()
multiplied_array = [element * 2 for element in mylist]
multiplied_array
for i in multiplied_array: 
  print(type(i))

