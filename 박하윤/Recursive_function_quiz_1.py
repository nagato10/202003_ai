#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

