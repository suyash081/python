#!/usr/bin/env python
# coding: utf-8

# In[1]:


# initializing string  
test_str = "we are learning python , we are programmers"
  
# initializing substring 
test_sub = "we"
  
# printing original string  
print("The original string is : " + test_str) 
  
# printing substring  
print("The substring to find : " + test_sub) 
  
# using list comprehension + startswith() 
# All occurrences of substring in string  
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 
  
# printing result  
print("The start indices of the substrings are : " + str(res)) 


# In[ ]:


use of isupper() and is lower()


# In[2]:


a= "I am learning python"
a.isupper()


# In[3]:


a= "i am learning python"
a.isupper()


# In[4]:


a= "I AM LEARNING PYTHON"
a.isupper()


# In[5]:


a= "i am learning python 3.7"
a.isupper()


# In[6]:


a= "#i am learning python"
a.isupper()


# In[7]:


a= "#I AM LEARNING PYTHON"
a.isupper()


# In[8]:


a= "I AM LEARNING PYTHON 3.7"
a.isupper()


# In[9]:


a= "I am learning python "
a.islower()


# In[11]:


a= "i am learning python"
a.islower()


# In[12]:


a= "i am learning python 3.7"
a.islower()


# In[13]:


a= "#i am learning python , batch 6"
a.islower()


# In[14]:


a= "19284 "
a.islower()


# In[15]:


a= "#$^&*^"
a.islower()


# In[ ]:




