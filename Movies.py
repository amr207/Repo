# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 00:54:37 2021

@author: AMR
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
#% matplotlib inline

#import dataset from file
main_df = pd.read_csv('tmdb-movies.csv')
df = main_df.copy()

#observe the data
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print('Number of duplicates = ' + str(df.duplicated().sum()))

#drop un-necessary columns
df.drop(['id','imdb_id','budget','revenue','original_title','cast','homepage',
         'director','tagline','keywords','overview','runtime','genres',
         'release_date','vote_count','vote_average','production_companies',
         'revenue_adj'],axis=1,inplace=True)

#celanse neede columns
df.drop_duplicates(inplace=True)
df=df[df['budget_adj']>0]
df.dropna(inplace=True)
print(df.describe())



print('------------Q1 START--------------')
#Q1: How many movies produced per year? and is any abnormal trends?
print(df['release_year'].value_counts())
plt.hist(df['release_year'])
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.title('Movies per Time')
plt.show()
print('------------Q1 END--------------')

print('------------Q2 START--------------')
#Q2: What is the relation between budget and film popularity?

df['budget_adj'].value_counts()

#as there are 5656 movies with 0 budget, which seems a data issue so will work
#on new data frame exluding movies with 0 budget

df.groupby('popularity')['budget_adj'].mean().plot(kind='line')
plt.xlabel('Movie Popularity')
plt.ylabel('Movie Budget')
plt.title('Popularity and Budget')
plt.show()
print('------------Q2 END--------------')


print('------------Q3 START--------------')
#Q3: Movies budget & years?
plt.bar(df['release_year'], df['budget_adj'])
plt.xlabel('Release Year')
plt.ylabel('Movie Budget')
plt.title("Movie's Budget over Time")
plt.show()
print('------------Q3 END--------------')


print('------------Q4 START--------------')
#Q4: Which years has better moveies (higher popularity)?
plt.bar(df['release_year'], df['popularity'])
plt.xlabel('Release Year')
plt.ylabel('Movie Popularity')
plt.title("Movie's Budget over Time")
plt.show()
print('------------Q4 END--------------')


#str(main_df['director']).split('|')[0].unique().count()
#main_df['director'].value_counts()

