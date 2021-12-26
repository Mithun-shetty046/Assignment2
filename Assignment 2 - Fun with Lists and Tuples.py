#!/usr/bin/env python
# coding: utf-8

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# 
# 
# 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# In[19]:


sample_input= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


# In[21]:


output=sorted(sample_input,key= lambda x: x[1])
print(output)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




