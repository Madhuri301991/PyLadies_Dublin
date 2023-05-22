#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('movies_complete.csv')


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.describe()


# In[6]:


df.head(10)


# In[7]:


df.revenue_musd.value_counts()


# In[8]:


df.revenue_musd.value_counts(dropna=False)


# In[9]:


df[df.title=="Waiting to Exhale"]


# In[10]:


df.drop(["poster_path"],axis=1)


# In[11]:


df["profit"]=df["revenue_musd"].sub(df["budget_musd"])


# In[12]:


df.head(10)


# In[13]:


df["return"]=df["revenue_musd"].div(df["budget_musd"])


# In[14]:


df.head(10)


# In[15]:


# Find all the movies of Bruce willis from begining to recent with genres as action


# In[16]:


a=df["genres"].str.contains("Action") 


# In[17]:


b=df["cast"].str.contains("Bruce Willis")


# In[18]:


df.loc[a & b]


# In[19]:


df.loc[a & b,["title","overview","release_date"]].sort_values(by="release_date",ascending=False)


# In[20]:


# Find movies with budget greater than 50 and revenue greater than 200


# In[21]:


df.loc[(df["budget_musd"]>50) & (df["revenue_musd"]>200)]


# In[22]:


df.loc[(df["budget_musd"]>50) & (df["revenue_musd"]>200),["title","genres","budget_musd","revenue_musd"]]


# In[23]:


#most successful pixar studio movies between 2010 and 2015 


# In[24]:


c=df["production_companies"].str.contains("Pixar")
c


# In[25]:


d=df["release_date"].between("2010-01-01","2014-12-31")
d


# In[26]:


df.loc[c & d,["title","release_date"]].sort_values(by='release_date',ascending=False).set_index("title")


# In[27]:


# Action or Thriller Movie and minimum Rating of 7.5 (most recent movies first)


# In[28]:


m=df["genres"].str.contains("Action") | df["genres"].str.contains("Thriller")
m


# In[29]:


n=df["original_language"]="en"
n


# In[30]:


o=df["vote_average"]>=7.5
o


# In[31]:


p=df["vote_count"]>=10
p


# In[32]:


df.loc[m & o & p,["title","genres","vote_average","vote_count","release_date"]]


# In[33]:


# Find the most successful Franchises


# In[34]:


df.groupby("belongs_to_collection").agg({"title":"count","popularity":["sum","mean"],"vote_count":"median"})


# In[35]:


# Most succesful directors


# In[36]:


df.groupby("director").revenue_musd.sum().nlargest(20)


# In[37]:


print("The END")


# In[1]:


#numpy 


# In[4]:


import numpy as np
study_hours=[10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
grade=[50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
student_data=np.array([study_hours,grade])
student_data


# In[ ]:


#simple case study


# In[6]:


import pandas as pd
import numpy as np

def login_table(p, n):

    p=p.drop(["Verified"],axis=1)
    df=pd.DataFrame(n, columns = ['id','Password'])
    p=p.merge(df[["Password"]],how="left",left_index=True,right_index=True)
    print(p)
    pass

p = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
n= np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(p, n)

