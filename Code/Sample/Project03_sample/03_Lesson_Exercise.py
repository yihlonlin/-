
# coding: utf-8

# In[ ]:


##############################################################
# coding:utf-8
import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
if __name__ == "__main__":
    corpus=["我 來自 台灣 義守大學", #第一類文本切詞後的結果，詞之間以空格隔開
        "他 來到 了 網易 杭研 大廈",     #第二類文本的切詞結果
        "小明 碩士 畢業 與 中央 研究院",  #第三類文本的切詞結果
        "我 愛 台灣 清華大學"]    #第四類文本的切詞結果
    #該類會將文本中的詞語轉換為詞頻矩陣，矩陣元素a[i][j] 表示j詞在i類文本下的詞頻
    vectorizer=CountVectorizer()
    #該類會統計每個詞語的tf-idf權值
    transformer=TfidfTransformer()
    #第一個fit_transform是計算tf-idf，第二個fit_transform是將文本轉為詞頻矩陣
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
    #獲取詞袋模型中的所有詞語
    word=vectorizer.get_feature_names()
    #將tf-idf矩陣抽取出來，元素a[i][j]表示j詞在i類文本中的tf-idf權重
    weight=tfidf.toarray()
    #列印每類文本的tf-idf詞語權重，第一個for遍歷所有文本，第二個for便利某一類文本下的詞語權重
    for i in range(len(weight)):
        print ("-------這裡輸出第",i,u"類文本的詞語tf-idf權重------")
        for j in range(len(word)):
            print(word[j],weight[i][j])

    vector = vectorizer.transform(["我 來到 台灣 義守大學"])
    print(vector.toarray())
    tfidf = transformer.fit_transform(vector)
    print(tfidf.toarray())

    vector = vectorizer.transform(["我 來到 義守大學"])
    print(vector.toarray())
    tfidf = transformer.fit_transform(vector)
    print(tfidf.toarray())

