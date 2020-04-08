#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


names =["Bob","Jessica","Mary","John","Mel"]


# In[17]:


print(names)


# In[18]:


bs=[1,1,0,0,1]


# In[19]:


grades=[76,95,77,78,99]


# In[20]:


ms=[2,1,0,0,0]


# In[21]:


phd=[0,1,0,0,0]


# In[22]:


gradelist=zip(names,grades,bs,ms,phd)


# In[23]:


print(gradelist)


# In[24]:


df=pd.DataFrame(data=gradelist,columns=["names","grades","bs","ms","phd"])


# In[25]:


print(df)


# In[30]:


df['grades'].mean()


# In[31]:


df['grades'].median()


# In[32]:


df['grades'].count()


# In[33]:


df['grades'].std()


# In[34]:


df['grades'].min()


# In[35]:


df['grades'].max()


# In[36]:


df['grades'].quantile(.25)


# In[37]:


df['grades'].quantile(.5)


# In[38]:


df['grades'].quantile(.75)


# In[39]:


df['grades'].median()


# In[40]:


df['grades'].mode()


# In[41]:


df['grades'].var()


# In[42]:


df['ms'].count()


# In[43]:


df['bs'].mean()


# In[44]:


df['phd'].max()

