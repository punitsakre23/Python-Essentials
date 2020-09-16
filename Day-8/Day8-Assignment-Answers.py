#!/usr/bin/env python
# coding: utf-8

# # Ans 1.

# In[16]:


def getrange(fibfun):
    def fibseries():
        print("Enter the range of Fibonacci Series")
        end = int(input("Enter ending no: "))
        fibfun(end)
    return fibseries


# In[17]:


@getrange
def fibonacciSeries(ending):
    starting = 0
    num = 0
    first = 1
    for i in range(ending):
        print("Fibonacci Series :", num)
        starting = first
        first = num
        num = starting + first


# In[18]:


fibonacciSeries()


# # Ans 2)

# In[60]:


file = open("Day8-AA","w")
file.write("Hey there!, How are you")
file.close()


# In[61]:


file = open("Day8-AA","r")
fileData = file.read()
print(fileData)
file.close()


# In[62]:


file = open("Day8-AA","a")
file.write("?")
file.close()


# In[63]:


file = open("Day8-AA","r")
fileData = file.read()
print(fileData)
file.close()


# In[64]:


file = open("Day8-AA", "r")
try :
    file.write("I am fine thankyou")
except :
    print("File is opened in read only mode, not writable!!!")
fileData = file.read()
print(fileData)
file.close()


# In[ ]:




