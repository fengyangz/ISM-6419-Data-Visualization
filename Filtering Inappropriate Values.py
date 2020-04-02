#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


names = ['Bob','Jessica','Mary','John','Mel'] 


# In[4]:


grades = [76,-2,77,78,101]


# In[5]:


GradeList = zip(names,grades)


# In[7]:


df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])


# In[8]:


df.loc[(df['Grades'] < 0 ,'Grades')] = 0


# In[9]:


df.loc[df['Grades'] <= 100]

