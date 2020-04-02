#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
Location = "datasets/HSD01.xlsx"
df = pd.read_excel(Location)


# In[8]:


df.columns = ['Area_name','STCOU','HSD010170F','HSD010170D']


# In[9]:


df.head()


# In[ ]:





# In[ ]:




