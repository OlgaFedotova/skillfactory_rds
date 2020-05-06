import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import collections


# In[77]:


data = pd.read_csv('data.csv')


# In[78]:


len(data)


# # Предобработка датасета

# In[79]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
data["profit"] = data["revenue"] - data["budget"] # создание новой колонки
data1 = data[data["profit"]>0] # только прибыльные фильмы
data["release_date"] = pd.to_datetime(data["release_date"]) # преобразование столбца с датой релиза
data["month"] = data["release_date"].dt.month #создадим колонку с месяцем
data["title_lenght"] = data["original_title"].str.len() #создадим колонку с длинной названия
data['lenth_word'] = data["original_title"].apply(lambda x: len(x.split())) #создадим колонку с колличеством слов в названии
data.head(3)


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[80]:


answer_ls.append(4)
data[['original_title', "imdb_id", 'budget']].query('budget == budget.max()')


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[81]:


answer_ls.append(2)
data[['original_title', "imdb_id", "runtime"]].query("runtime == runtime.max()")


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[82]:


answer_ls.append(3)
data[['original_title', "imdb_id", "runtime"]].query("runtime == runtime.min()")


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[83]:


answer_ls.append(2)
round(data["runtime"].mean())


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[84]:


answer_ls.append(1)
round(data["runtime"].median())


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[85]:


answer_ls.append(5)
data[['original_title', "imdb_id", "profit"]].query("profit == profit.max()")


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[86]:


answer_ls.append(2)
data[['original_title', "imdb_id", "profit"]].query("profit == profit.min()")


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[87]:


answer_ls.append(1)
data[data.profit>0].shape[0]


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[88]:


answer_ls.append(4)
data.loc[data.profit == data[data["release_year"] == 2008]["profit"].max()]


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[89]:


answer_ls.append(5)
data.loc[data.profit == data.query("release_year >= 2012 & release_year <= 2014")["profit"].min()]


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[90]:


answer_ls.append(3)
c = collections.Counter()
for elements in data["genres"].str.split("|"):
    for genre in elements:
        c[genre]+=1
c.most_common()[0]


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[91]:


answer_ls.append(1)
count_films = collections.Counter()
for elements in data[data["profit"]>0]["genres"].str.split("|"):
    for genre in elements:
        count_films[genre]+=1       
count_films.most_common()[0]


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[92]:


answer_ls.append(3)
# version 1
c = collections.Counter()
for elements in data["director"].str.split("|"):
    for director in elements:
        c[director]+=1
c.most_common()[0]


# In[93]:


# version 2
data.groupby(['director']).agg('count')['imdb_id'].sort_values(ascending=False).reset_index().head(1)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[94]:


answer_ls.append(4)
# version 1
c = collections.Counter()
for elements in data[data.profit > 0]["director"].str.split("|"):
    for director in elements:
        c[director]+=1        
c.most_common()[0]


# In[95]:


# version 2
data[data.profit > 0].groupby(['director']).agg('count')['imdb_id'].sort_values(ascending=False).reset_index().head(1)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[96]:


answer_ls.append(5)
data.groupby('director')['profit'].sum().reset_index()[["director", "profit"]].query("profit == profit.max()")


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[97]:


answer_ls.append(1)
new_data = pd.DataFrame(columns=('actor','profit', "year", "budget"))
for index, line in data.iterrows():
    for actor in line['cast'].split('|'):
        new_data = new_data.append({'actor': actor, 'profit': line['profit'], 'year': line['release_year'], 'budget': line['budget']}, ignore_index=True)
new_data.groupby(['actor'])['profit'].sum().sort_values(ascending=False).reset_index().head(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[98]:


answer_ls.append(3)
new_data[new_data["year"] == 2012].groupby(['actor'])['profit'].sum().sort_values(ascending=True).reset_index().head(1)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[99]:


answer_ls.append(3)
# version 1
c = collections.Counter()
for item in data[data.budget > data.budget.mean()]["cast"].str.split("|"):
    for actor in item:
        c[actor]+=1
c.most_common()[0]


# In[100]:


# version 2
new_data[new_data["budget"] > new_data["budget"].mean()]['actor'].value_counts().reset_index().head(1)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[101]:


answer_ls.append(2)
count = collections.Counter()
for item in data[data.cast.str.contains('Nicolas Cage',case=False)]["genres"].str.split("|"):
    for genre in item:
        count[genre]+=1
count.most_common()[0]


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[102]:


answer_ls.append(1)
count_companies = collections.Counter()
for line in data["production_companies"].str.split("|"):
    for company in line:
        count_companies[company]+=1
count_companies.most_common()[0]


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[103]:


answer_ls.append(4)
count_companies_2015 = collections.Counter()
for line in data[data["release_year"] == 2015]["production_companies"].str.split("|"):
    for company in line:
        count_companies_2015[company]+=1
count_companies_2015.most_common()[0]


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[104]:


answer_ls.append(2)
count_companies = collections.Counter()
for index, line in data[data.genres.str.contains("Comedy")].iterrows():
    for company in line["production_companies"].split("|"):
        count_companies[company] += line["profit"]
count_companies.most_common()[0]


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[105]:


answer_ls.append(3)
count_companies = collections.Counter()
for index, line in data[data["release_year"] == 2012].iterrows():
    for company in line["production_companies"].split("|"):
        count_companies[company] += line["profit"]
count_companies.most_common()[0]


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[106]:


answer_ls.append(1)
data[data.production_companies.str.contains("Paramount Pictures")][['original_title', "imdb_id", "profit"]].query("profit == profit.min()")


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[107]:


answer_ls.append(5)
data.groupby(["release_year"])["profit"].sum().sort_values(ascending=False).reset_index().head(1)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[108]:


answer_ls.append(1)
data[data.production_companies.str.contains("Warner Bros")].groupby(["release_year"])["profit"].sum().sort_values(ascending=False).reset_index().head(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[109]:


answer_ls.append(4)
data.groupby(data["month"])["imdb_id"].count().sort_values(ascending=False).reset_index().head(1)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[110]:


answer_ls.append(2)
data[(data["month"] <= 8) & (data["month"] >= 6)]["original_title"].count()


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[111]:


answer_ls.append(5)
# version 1
count_winter = collections.Counter()
for line in data[(data["month"] == 12) | (data["month"] <= 2)]["director"].str.split("|"):
    for director in line:
        count_winter[director]+=1
count_winter.most_common()[0]


# In[112]:


# version 2
data[data.month.isin([1, 2, 12])].groupby('director').agg('count').sort_values('imdb_id', ascending=False).head(1)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[113]:


answer_ls.append(2)
new_data = data.groupby(['release_year', 'month']).agg('sum')
data_max = new_data.groupby(['release_year', 'month']).agg('sum').groupby('release_year').agg('max')[['profit']].rename(columns ={"profit": "max_profit"})
new_data.reset_index(inplace=True)
new_data = new_data.merge(data_max, on='release_year')
new_data[new_data.profit == new_data.max_profit].month.value_counts().sort_values(ascending=False)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[114]:


answer_ls.append(5)
count = collections.Counter()  
new_data = pd.DataFrame(columns=('company','lenth'))
for index, line in data.iterrows():
    for company in line['production_companies'].split('|'):
        new_data = new_data.append({'company': company, 'lenth': line['title_lenght']}, ignore_index=True)
new_df = new_data.groupby(['company'])['lenth'].agg(["sum", "count"])
new_df["average"] = new_df["sum"] / new_df["count"]
new_df.sort_values(ascending=False, by=["average"]).reset_index().head(1)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[115]:


answer_ls.append(5)
count = collections.Counter()  
df = pd.DataFrame(columns=('company','word_lenth'))
for index, line in data.iterrows():
    for company in line['production_companies'].split('|'):
        df = df.append({'company': company, 'word_lenth': line['lenth_word']}, ignore_index=True)
df2 = df.groupby(['company'])['word_lenth'].agg(["sum", "count"])
df2["average"] = df2["sum"] / df2["count"]
df2.sort_values(ascending=False, by=["average"]).reset_index().head(1)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[116]:


answer_ls.append(3)
import collections
count = collections.Counter()
words = 0
for name in data["original_title"]:
    for word in name.split():
        word = word.lower()
        count[word]+=1
list_words = list(count)
for word in list_words:
    words += 1
words


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[117]:


answer_ls.append(1)
data[["original_title", "vote_average"]].sort_values(ascending=False, by=["vote_average"]).reset_index().head(19)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[118]:


answer_ls.append(5)
import itertools
import collections
count = collections.Counter() 
for line in data["cast"].str.split('|'):
    for pair in list(itertools.combinations(line, 2)):
        count[pair]+=1
count.most_common()[0]


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[119]:


answer_ls.append(4)
count = lambda x: len([ i for i in x if i  > 0])
data['profit_films'] = data['profit']
new_data = data.groupby('director').aggregate({"imdb_id": len, "profit_films": count})
new_data['probability'] = new_data.profit_films / new_data.imdb_id
new_data.sort_values(ascending=False, by = "profit_films").reset_index().head(10)


# # Submission

# In[120]:


len(answer_ls)


# In[121]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




