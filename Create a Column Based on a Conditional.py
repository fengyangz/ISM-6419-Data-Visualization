#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


Location = "datasets/gradedata.csv" 


# In[9]:


df = pd.read_csv(Location)


# In[10]:


df.head()


# In[11]:


df['isBussy'] = np.where((df['exercise']>3) & (df['hours'] > 17),'yes', 'no')


# In[12]:


df.tail(10)

