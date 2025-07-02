#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# In[35]:


n = 6
dataset = {f"experience{i}": np.random.randn(100) for i in range(n)}


# In[38]:


def graphique(dataset):
    x = [i for i in range(100)]
    plt.figure(figsize=(12, 3*n))
    for i in range(n):
        plt.subplot(n,1,i+1)
        plt.plot(x, dataset[f"experience{i}"])
        plt.title(f"expérience {i}")
    plt.show()


# In[39]:


graphique(dataset)


# In[ ]:




