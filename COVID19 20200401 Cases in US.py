#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[121]:


Location = "datasets/04-01-2020.csv"


# In[122]:


df = pd.read_csv(Location)


# In[123]:


df.head()


# In[151]:


import pandas as pd


# In[118]:


Location = "datasets/04-01-2020.csv"


# In[119]:


df = pd.read_csv(Location)


# In[140]:


df.columns = ['Province_State','Confirmed','Deaths','Recovered','Active']


# In[149]:


print 'COVID-19 2020/04/01 Cases in US'


# In[144]:


df

