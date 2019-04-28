#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandas_profiling
import numpy as np


# In[2]:


conda install -c anaconda pandas-profiling


# In[3]:


import pandas_profiling


# In[4]:


df = pd.read_csv("https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD", parse_dates=['year'], encoding='UTF-8')

# Note: Pandas does not support dates before 1880, so we ignore these for this analysis
df['year'] = pd.to_datetime(df['year'], errors='coerce')

# Example: Constant variable
df['source'] = "NASA"

# Example: Boolean variable
df['boolean'] = np.random.choice([True, False], df.shape[0])

# Example: Mixed with base types
df['mixed'] = np.random.choice([1, "A"], df.shape[0])

# Example: Highly correlated variables
df['reclat_city'] = df['reclat'] + np.random.normal(scale=5,size=(len(df)))

# Example: Duplicate observations
duplicates_to_add = pd.DataFrame(df.iloc[0:10])
duplicates_to_add[u'name'] = duplicates_to_add[u'name'] + " copy"

df = df.append(duplicates_to_add, ignore_index=True)


# In[6]:


pandas_profiling.ProfileReport(df)


# In[ ]:




