#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from random import *


# In[2]:


def initialisation (l, c):
    res = np.random.randn(l, c)
    res1 = np.ones((l, 1))
    res = np.concatenate((res, res1), axis = 1)
    return res


# In[4]:


print(initialisation(4,3))


# In[ ]:




