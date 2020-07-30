#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gTTS')


# In[7]:


from gtts import gTTS
text=input("enter the text to be converted:  ")

speech=gTTS(text)
speech.save("speechtotext.mp3")


# In[ ]:




