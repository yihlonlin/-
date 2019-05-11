
# coding: utf-8

# In[6]:


from keras.preprocessing.text import Tokenizer
# define 5 documents
docs = ['Well done!',
        'Good work',
        'Great effort',
        'nice work',
        'Excellent!']
# create the tokenizer
t = Tokenizer()
# fit the tokenizer on the documents
t.fit_on_texts(docs)
# summarize what was learned
print(t.word_counts)
print(t.document_count)
print(t.word_index)
#print(t.word_index['well'])
print(t.word_docs)
# integer encode documents
encoded_docs = t.texts_to_matrix(docs, mode='count')
print(encoded_docs)


# In[1]:


#http://beanobody.blogspot.tw/2015/06/jieba.html
import jieba
seg_list = jieba.cut("我義守大學的老師", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))


# In[3]:


#encoding=utf-8
import jieba
jieba.set_dictionary('dict.txt.big')
content = open('lyric_tw.txt', 'rb').read() #str
print("Input(unicode):", content)
#print("Input(utf-8):", content.decode('utf8'))
words = jieba.cut(content, cut_all=False)
print('Output Full Mode:')
for word in words:
    print(word)
type(word)


# In[12]:


#encoding=utf-8
import jieba
jieba.set_dictionary('dict.txt.big')
content = open('lyric_tw.txt', 'r', encoding='UTF-8').read() #str
print("Input:", content)
words = jieba.cut(content, cut_all=False)
print('Output Full Mode:')
for word in words:
    print(word)


# In[7]:


#encoding=utf-8
import jieba
import numpy as np
plain_text = []
tokenset = set()
#content = open('lyric.txt', 'r').read()
fin = open('lyric.txt', 'r', encoding='UTF-8')
chinese_punctuations = ['，', '。', '：', '；', '?','（', '）', '「', '」', '！', '“', '”', '\n']
stopwords = ['你','我','他','她','它']
for eachLine in fin:
    tmp_line = []
    tokens = jieba.cut(eachLine)
    for word in tokens:
        if((word not in chinese_punctuations) and (word not in stopwords)):
            tokenset.add(word)
            tmp_line.append(word)
    plain_text.append(tmp_line)
fin.close()
tokenlist = list(tokenset)
print(tokenlist)

