#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np


# In[17]:


import pandas as pd


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


Location = 'datasets/gradedata.csv'


# In[21]:


df = pd.read_csv(Location)


# In[22]:


df.head()


# In[34]:


plt.scatter(df['hours'], df['grade'])


# In[ ]:




