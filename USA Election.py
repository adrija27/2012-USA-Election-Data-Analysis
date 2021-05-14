#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as og
from plotly.offline import init_notebook_mode,download_plotlyjs,plot,iplot 


# In[2]:


init_notebook_mode(connected=True)


# In[3]:


df=pd.read_csv('2012_Election_Data.csv')


# In[4]:


df.head()


# In[5]:


data=dict(type='choropleth',
          locations=df['State Abv'],
          colorscale='ylorrd',
          locationmode='USA-states',
          text=df['State'],
          z=df['Voting-Age Population (VAP)'],
          colorbar={'title':'2012 USA VAP'},
          marker=dict(line=dict(color='rgb(0,0,0)',width=1))
         )


# In[6]:


layout=dict(title= '2012 USA VAP variations over states',
            geo=dict(scope='usa',
                     showlakes=True,
                     lakecolor='rgb(85,173,240)')
           )


# In[7]:


choromap=og.Figure(data=[data],layout=layout)


# In[8]:


iplot(choromap)


# In[9]:


def point(x):
    return float(x.replace(',',''))
df[['Voting-Eligible Population (VEP)']]=list(df['Voting-Eligible Population (VEP)'].apply(point))


# In[10]:


df.head()


# In[11]:


data=dict(type='choropleth',
          locations=df['State Abv'],
          colorscale='ylorrd',
          locationmode='USA-states',
          text=df['State'],
          z=df['Voting-Eligible Population (VEP)'],
          colorbar={'title':'2012 USA VEP'},
          marker=dict(line=dict(color='rgb(0,0,0)',width=1))
         )


# In[12]:


layout=dict(title= '2012 USA VEP variations over states',
            geo=dict(scope='usa',
                     showlakes=True,
                     lakecolor='rgb(85,173,240)')
           )


# In[13]:


choromap=og.Figure(data=[data],layout=layout)


# In[14]:


iplot(choromap)

