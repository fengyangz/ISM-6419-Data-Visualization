#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[17]:


import os


# In[24]:


os.getcwd()


# In[29]:


os.chdir('C:\\Users\\fanya\\datasets')


# In[30]:


Location = "C:\\Users\\fanya\\datasets\\House Hold.xls"


# In[31]:


df =  pd.read_excel(Location)


# In[32]:


df.head()

