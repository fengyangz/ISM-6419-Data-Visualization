#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


Location = "datasets/gradedata.csv"


# In[5]:


df = pd.read_csv(Location)


# In[6]:


df.head()


# In[7]:


df.hist()


# In[8]:


df.hist(column="age",by="gender")


# In[ ]:




