#!/usr/bin/env python
# coding: utf-8

# while loon sum of n numbers

# In[3]:


sum = 0 
value = 1
print ("enter the number ")
num = int (input())

print("you have entered " ,  num )

while value <= num :
        sum = sum +value
        value = value + 1
        
    
print("sum upto " , num , "number is" , sum)


# prime no .

# In[4]:


print("enter the number")
value =int(input(""))


if value > 1 :

    for i in range(2, value) :
        if (value % i) == 0 :
            print("The number" ,value, "is not a Prime no .")
            break 
    else :
        print("The number" , value , "is a Prime no ." )


# In[ ]:




