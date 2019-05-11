
# coding: utf-8

# In[2]:


from nltk.tokenize import word_tokenize
import nltk
sent = "the the the dog, dog some other words that we do not care about"
list=[word for word in word_tokenize(sent)]
vacabulary = sorted(set(list))
freq = nltk.FreqDist(list)
freq.plot()


# In[4]:


stopwords=[",","the"]
list=[word for word in word_tokenize(sent) if word not in stopwords]
print(list)


# In[ ]:


#stopword
#https://github.com/dongxiexidian/Chinese/blob/master/stopwords.dat
#https://github.com/dongxiexidian/Chinese/tree/master/dict

