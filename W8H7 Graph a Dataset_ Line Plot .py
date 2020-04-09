#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[5]:


grades = [76,83,77,78,95]


# In[6]:


data = {"Names": names,"Grades": grades}


# In[7]:


GradeList = zip(names,grades)


# In[8]:


GradeList


# In[9]:


df = pd.DataFrame(data,columns = ['Names','Grades'])


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df.plot()


# In[21]:


import matplotlib.pyplot as plt
df.plot()
displayText = "Wow!" 
xloc = 0
yloc = df['Grades'].min() 
xtext = 8
ytext = -150 
plt.annotate(displayText,
                       xy=(xloc, yloc), 
             arrowprops=dict(facecolor='black',
                             shrink=0.05),
                       xytext=(xtext,ytext), 
                       xycoords=('axes fraction', 'data'), 
                       textcoords='offset points')


# In[ ]:





# In[ ]:




