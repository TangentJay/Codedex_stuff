#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter


# In[4]:


with open('timoreilly.json', 'r') as file:
    data_list = json.load(file)


# In[5]:


titles = [item.get('title', '') for item in data_list]
contents = [item.get('content', '') for item in data_list]


text = ' '.join(titles + contents)


tokens = word_tokenize(text)


token_freq = Counter(tokens)


sorted_token_freq = sorted(token_freq.items(), key=lambda x: x[1], reverse=True)


# In[6]:


if sorted_token_freq:
   
    ranks, frequencies = zip(*enumerate([freq for token, freq in sorted_token_freq], 1))

    # Plot Zipf's curve
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, marker='.')
    plt.title("Zipf's Curve")
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("No tokens found.")


# In[ ]:




