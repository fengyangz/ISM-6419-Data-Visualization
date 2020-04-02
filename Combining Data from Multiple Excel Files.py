#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


import os


# In[25]:


os.getcwd()


# In[4]:


import numpy as np


# In[5]:


import glob


# In[26]:


all_data = pd.DataFrame()


# In[29]:


all_data = pd.DataFrame()
for f in glob.glob("C:\\Users\\fanya\\datasets\\weekly_call_data\\weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True) 


# In[30]:


all_data.describe()


# In[ ]:




