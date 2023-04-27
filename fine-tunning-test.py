#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import os

df = pd.read_csv("/Users/komal/downloads/questions-list-1.csv")
df.head()


# In[72]:


# keep only the 1st and 2nd columns using iloc indexing
df = df.iloc[:, :2]

# write the new DataFrame to a CSV file
# df.to_csv('questions_new.csv', index=False)


# In[73]:


# rename multiple columns using a dictionary of old and new names
new_names = {'Question': 'prompt', 'Answer': 'completion'}
df = df.rename(columns=new_names)


# In[74]:


df


# In[75]:


df.to_json("question-ans.jsonl", orient='records', lines=True)


# In[76]:


import openai


# In[77]:


openai.api_key = "...."


# In[78]:


openai.api_key
os.environ['OPENAI_API_KEY'] = openai.api_key


# In[79]:


get_ipython().system('openai tools fine_tunes.prepare_data -f question-ans.jsonl -q')


# In[80]:


get_ipython().system('openai api fine_tunes.create -t "question-ans_prepared.jsonl" -m ada')


# In[81]:


get_ipython().system('openai api fine_tunes.follow -i ft-fWMcVjVyWXUW6NTZYSN8Q00N')


# In[82]:


get_ipython().system('openai api fine_tunes.list')


# In[83]:


get_ipython().system('openai api fine_tunes.results -i ft-fWMcVjVyWXUW6NTZYSN8Q00N > result.csv')


# In[85]:


results = pd.read_csv('result.csv')
# results[results['classification/accuracy'].notnull()].tail(1)


# In[87]:


results.head(20)


# In[99]:


ft_model = 'ada:ft-personal-2023-04-25-12-00-27'
res = openai.Completion.create(model=ft_model, prompt="language used in rapid trance", max_tokens=100, temperature=0)
res['choices'][0]['text']

