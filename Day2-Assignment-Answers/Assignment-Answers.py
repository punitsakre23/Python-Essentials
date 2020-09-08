#!/usr/bin/env python
# coding: utf-8

# # Q1. List and it's default functions 

# In[1]:


lst = ["Keyboard", 23.123, "ESP8266", 789, .007]


# In[2]:


lst.append("Keyboard")
lst


# In[3]:


lst.count("Keyboard")


# In[4]:


lst.index(789)


# In[5]:


lst.reverse()
lst


# In[6]:


lst.clear()
lst


# # Q2. Dictionary and it's default functions

# In[7]:


dct = {
    "name" : "Thor",
    "age" : 1500,
    "planet" : "Asgard",
    "weapon" : "Stormbreaker"
}


# In[8]:


dct.get('name')


# In[9]:


dct.items()


# In[10]:


dct.keys()


# In[11]:


dct.values()


# In[12]:


dct.pop("planet")


# In[13]:


dct


# # Q3. Sets and it's default functions 

# In[14]:


st = {"Batsman", 101, "Bowler", 007.1, "Fielder", "Batsman"}


# In[15]:


st


# In[16]:


st.add(2554816)
st


# In[17]:


st.discard("Fielder")
st


# In[18]:


st1 = {"Captain", 101, "Bowler", 007.1, "Fielder", "Batsman"}


# In[19]:


st.difference(st1)


# In[20]:


st1.difference(st)


# In[21]:


st.difference_update(st1)
st


# In[22]:


st.update(st1)
st


# # Q4. Tuple and explore default methods 

# In[23]:


tupl = ("Yahoo", .25, "Google", 555, "Bing")


# In[24]:


tupl


# In[25]:


tupl.count(0.25)


# In[26]:


tupl.index(555)


# In[27]:


tpl = tuple(("ThunderBolt", "ShadowKing", "DareDevil"))


# In[28]:


tpl


# In[29]:


len(tpl)


# In[30]:


tl = tupl + tpl


# In[31]:


tl


# # Q5. String and explore default methods

# In[32]:


string = "hey! there, how you doing?"


# In[33]:


string


# In[34]:


string.capitalize()


# In[35]:


string.center(50)


# In[36]:


string.count("h")


# In[37]:


string.endswith("?")


# In[38]:


string.swapcase()


# In[ ]:




