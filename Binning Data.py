#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


Location = "datasets/gradedata.csv" 


# In[8]:


df = pd.read_csv(Location) 


# In[9]:


df.head()


# In[10]:


# Create the bin dividers


# In[11]:


bins = [0, 80, 100]


# In[12]:


# Create names for the four groups 


# In[13]:


group_names = ['S','U']


# In[15]:


df['S/Ugrade'] = pd.cut(df['grade'], bins,labels=group_names)


# In[16]:


df


# In[ ]:




