#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1


# In[1]:



def fun1(x):
    a = [0 for i in range(x.count(0))]
    lst = [ i for i in x if i != 0]
    lst.extend(a)
    return(lst)

print(fun1([0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]))


# In[ ]:


#assignment 2


# In[ ]:





# In[10]:


x = [2,9,4,6]
y = [7,8,3,5]
z = []
maxi = x[0]
pos = 0
print('x: '+str(x))
print('y: '+str(y))

for i in range(len(y)):
  x.append(y[i])

for j in range(len(x)-1):
    maxi = x[0]
    for i in range(len(x)):
        if maxi > x[i]:
            maxi = x[i]
            pos = i
    z.append(maxi)
    del x[pos]
z.append(x[0])
print('z: '+str(z))


# In[ ]:




