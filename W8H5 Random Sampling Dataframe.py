#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


Location = 'datasets/gradedata.csv'


# In[4]:


df = pd.read_csv(Location)


# In[5]:


df.tail()


# In[6]:


df.take(np.random.permutation(len(df))[:500])

