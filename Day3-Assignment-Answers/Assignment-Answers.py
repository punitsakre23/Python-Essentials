#!/usr/bin/env python
# coding: utf-8

# # Answer 1.

# In[6]:


altitude = int(input("Current Altitude : "))

if altitude <= 1000:
    print("Safe to land")
elif altitude < 5000:
    print("Bring down to 1000ft")
else :
    print("Turn Around")


# # Ans 2)

# In[36]:


num = 200

for num in range (2,201):
    count = 0
    for i in range (2,num):
        if  (num%i == 0):
            count = 1
    if (count == 0):
        print("Prime no.s are :", num)


# In[ ]:





# In[ ]:




