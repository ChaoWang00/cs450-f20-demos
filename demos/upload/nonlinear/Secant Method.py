#!/usr/bin/env python
# coding: utf-8

# # Secant Method

# In[1]:


import numpy as np
import matplotlib.pyplot as pt


# Here's a function: (Look here! No derivative.)

# In[3]:


def f(x):
    return x**3 - x +1

xmesh = np.linspace(-2, 2, 100)
pt.ylim([-3, 10])
pt.grid()
pt.plot(xmesh, f(xmesh))


# In[7]:


guesses = [2, 1.5]


# Evaluate this cell many times in-place (using Ctrl-Enter)

# In[30]:



# grab last two guesses
x = guesses[-1]
xbefore = guesses[-2]

slope = (f(x)-f(xbefore))/(x-xbefore)

# plot approximate function
pt.plot(xmesh, f(xmesh))
pt.plot(xmesh, f(x) + slope*(xmesh-x))
pt.plot(x, f(x), "o")
pt.plot(xbefore, f(xbefore), "o")
pt.ylim([-3, 10])
pt.axhline(0, color="black")

# Compute approximate root
xnew = x - f(x) / slope
guesses.append(xnew)
print(xnew)


# In[ ]:




