
# coding: utf-8

# In[6]:


from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())


# In[7]:


from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.vocabulary_)
word = vectorizer.get_feature_names()
print(word)
print(X.toarray())
X = vectorizer.transform([corpus[0]])
print(X.toarray())


# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog.", "The dog.", "The fox"]
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
vector = vectorizer.transform([text[1]])
#summarize encoded vector
print(vector.shape)
print(vector.toarray())


# In[6]:


import numpy as np
import math
tf_the=1/2
tf_dog=1/2
idf_the=math.log((3+1)/(3+1))+1
idf_dog=math.log((3+1)/(2+1))+1
dis=math.sqrt((id_the*idf_the)*(id_the*idf_the)+(id_dog*idf_dog)*(id_dog*idf_dog))
tfidf_the=(id_the*idf_the)/dis
tfidf_dog=(id_dog*idf_dog)/dis
print(tfidf_the)
print(tfidf_dog)


# In[2]:


import math, re
import string
text = ["The quick brown fox jumped over the lazy dog.", "The dog.", "The fox"]
from nltk.tokenize import word_tokenize
# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
txt =re_punc.sub('', text[0])
tokens = word_tokenize(txt)
tokens = word_tokenize(txt.lower())
words = vectorizer.get_feature_names()
for word in words:
    if_=tokens.count(word)/len(tokens)
    print(word,':',if_)


# In[1]:


import math
print("brown",':',math.log((3+1)/(1+1))+1)
print("dog",':',math.log((3+1)/(2+1))+1)
print("fox",':',math.log((3+1)/(2+1))+1)
print("jumped",':',math.log((3+1)/(1+1))+1)
print("lazy",':',math.log((3+1)/(1+1))+1)
print("over",':',math.log((3+1)/(1+1))+1)
print("quick",':',math.log((3+1)/(1+1))+1)
print("the",':',math.log((3+1)/(3+1))+1)


# In[81]:


from sklearn.feature_extraction.text import HashingVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = HashingVectorizer(n_features=20)
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

