#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd


# In[26]:


import matplotlib.pyplot as plt


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[29]:


absences = [3,0,1,0,8]


# In[30]:


detentions = [2,1,0,0,1]


# In[31]:


warnings = [2,1,5,1,2]


# In[32]:


GradeList = zip(names,absences,detentions,warnings)


# In[33]:


columns=['Names','Absences','Detentions','Warnings']


# In[34]:


df = pd.DataFrame(data = GradeList,columns=columns)


# In[35]:


df


# In[36]:


df['TotalDemerits']=df['Absences']+df['Detentions']+df['Warnings']


# In[37]:


df


# In[38]:


plt.pie(df['TotalDemerits'])


# In[39]:


plt.pie(df['TotalDemerits'],labels=df['Names'],explode=(0,0,0,0.15,0),startangle=90,autopct='%1.1f%%')


# In[ ]:





# In[ ]:




