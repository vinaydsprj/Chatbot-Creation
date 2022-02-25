#!/usr/bin/env python
# coding: utf-8

# In[1]:
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np


# In[2]:


import pickle


# In[3]:


pickled_model = pickle.load(open('model.pkl', 'rb'))


# In[4]:


#pickled_model.predict(u[0:1])[0]


# In[5]:


with open('dictOfWords1.pickle', 'rb') as handle:
    d1= pickle.load(handle)
#d1


# In[6]:


with open('dictOfWords2.pickle', 'rb') as handle:
    d2= pickle.load(handle)
#d2


# In[7]:


with open('dictOfWords3.pickle', 'rb') as handle:
    d3= pickle.load(handle)
#d3


# In[8]:


with open('dictOfWords4.pickle', 'rb') as handle:
    d4= pickle.load(handle)
#d4


# In[10]:
def delay_prediction_fun(lst,dst,trn,day):

						local_station=lst
						destination_station=dst
						day=day
						train_number=int(trn)


						# In[11]:


						i1=d1[local_station]
						i2=d2[destination_station]
						i3=d3[train_number]
						i4=d4[day]
						#print(i1,i2,i3,i4)


						# In[12]:


						u=pd.read_csv("user_pred.csv")


						# In[13]:


						u=u.drop(['Unnamed: 0'], axis=1)


						# In[14]:


						#12	88	197	5
						u[:1]['tiploc']=i1
						u[:1]['dst_loc']=i2
						u[:1]['Train NO.']=i3
						u[:1]['DAY']=i4


						# In[15]:


						#pickled_model = pickle.load(open('model.pkl', 'rb'))


						# In[16]:


						result=pickled_model.predict(u[0:1])[0]


						# In[17]:


						#print("the delay is ",result)

						return result


						# In[ ]:




