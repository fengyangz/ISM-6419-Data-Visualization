#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


from sqlalchemy import create_engine


# In[6]:


# Connect to sqlite db


# In[11]:


db_file = r'salesdata.db' 


# In[12]:


engine = create_engine(r"sqlite:///{}".format(db_file)) 


# In[13]:


sql = "select * from scores;" 


# In[14]:


sales_data_df = pd.read_sql(sql, engine) 


# In[15]:


sales_data_df.head()


# In[ ]:




