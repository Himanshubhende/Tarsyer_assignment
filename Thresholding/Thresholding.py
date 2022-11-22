#!/usr/bin/env python
# coding: utf-8

# ## 3) Thresholding

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# ### Simple Thresholding :

# In[2]:


img = cv2.imread('Task_3.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Orignal.jpg",img)


# #### Binary Thresholding :

# In[3]:


ret,BINARY = cv2.threshold(img,60,255,cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(BINARY, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Binary.jpg",BINARY)


# #### Binary_Inv Thresholding :

# In[4]:


ret,BINARY_INV = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(cv2.cvtColor(BINARY_INV, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Binary_Inv.jpg",BINARY_INV)


# #### Trunc Thresholding :

# In[5]:


ret,TRUNC = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(cv2.cvtColor(TRUNC, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Trunc.jpg",TRUNC)


# #### Tozero Thresholding :

# In[6]:


ret,TOZERO = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
plt.imshow(cv2.cvtColor(TOZERO, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Tozero.jpg",TOZERO)


# #### Tozero_inv Thresholding :

# In[7]:


ret,TOZERO_INV = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(cv2.cvtColor(TOZERO_INV, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_simple_Tozero_Inv.jpg",TOZERO_INV)


# ### Adaptive Thresholding :

# In[8]:


img = cv2.imread('Task_3.jpg',1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# #### Adaptive Mean Thresholding :

# In[9]:


AMT = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,199,2)
plt.imshow(cv2.cvtColor(AMT, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_adaptive_Mean.jpg",AMT)


# #### Adaptive Gaussian Thresholding :

# In[10]:


AGT = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
plt.imshow(cv2.cvtColor(AGT, cv2.COLOR_BGR2RGB))
cv2.imwrite("Task_3_adaptive_Gaussian.jpg",AGT)


# In[ ]:





# In[ ]:




