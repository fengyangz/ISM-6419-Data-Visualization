#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Location = "datasets/gradedata.csv"


# In[3]:


df = pd.read_csv(Location)


# In[4]:


df.head()


# In[6]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0


# In[7]:


df['gender_val'] = df['gender'].apply(score_to_numeric)


# In[8]:


df.tail()


# In[9]:


df_gender = pd.get_dummies(df['gender'])


# In[10]:


df_gender.tail()


# In[11]:


df_new = pd.concat([df,df_gender],axis=1)


# In[12]:


df_new.tail()


# In[13]:


import statsmodels.formula.api as sm


# In[14]:


result = sm.ols(formula='grade~gender',data=df).fit()


# In[15]:


result.summary()

