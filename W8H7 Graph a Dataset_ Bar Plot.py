#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import pandas as pd


# In[4]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[5]:


status = ['Senior','Freshman','Sophomore','Senior','Junior']


# In[6]:


grades = [76,95,77,78,99]


# In[22]:


GradeList = zip(status,grades)


# In[23]:


df = pd.DataFrame(data=GradeList, columns=['Status','Grades'])


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


df.plot(kind='bar')


# In[26]:


df2 = df.set_index(df['Status'])


# In[27]:


df2.plot(kind='bar')


# In[ ]:




