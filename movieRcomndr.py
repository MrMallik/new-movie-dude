#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


df = pd.read_csv("movie_dataset.csv")


# In[3]:


features = ["keywords", "cast", "genres", "director"]


# In[4]:


def combine_features(row):
    return row["keywords"] + " " + row["cast"] + " " + row["genres"] + " " + row["director"]


# In[5]:


for feature in features:
    df[feature] = df[feature].fillna('')
    
df["combined_features"] = df.apply(combine_features,axis=1)


# In[7]:


cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object


# In[8]:


cosine_sim = cosine_similarity(count_matrix)


# In[17]:


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


# In[25]:

def getMovie():
    return input("Enter your favourite movie : ")

def getRecommendations(movie_user_likes):

    films = dict()

    try:
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies = list(enumerate(cosine_sim[movie_index]))

        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

        i=0
        print("Top 5 similar movies to "+movie_user_likes+" are:\n")
        for element in sorted_similar_movies:
            #print(get_title_from_index(element[0]))
            films[i] = (get_title_from_index(element[0]))
            i=i+1
            if i>4:
                return films
    except IndexError:
        print("We don't have the specified title in our records!")


if __name__ == '__main__':
    myDict = getRecommendations(getMovie())
    for k,v in myDict.items():
        print(k+1, v)

# In[ ]:




