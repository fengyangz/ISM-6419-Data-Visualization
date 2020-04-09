#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


Location = "datasets/gradedata.csv"


# In[7]:


df = pd.read_csv(Location)


# In[29]:


df.head()


# In[37]:


df = df.sort_values(by='fname',ascending=[True])


# In[38]:


df.head()


# In[44]:


df = df.sort_values(by='age',ascending=[True])


# In[45]:


df.head()


# In[48]:


df = df.sort_values(by='grade',ascending=[0])


# In[49]:


df.head()


# In[ ]:




