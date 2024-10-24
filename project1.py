#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:34:14 2024

@author: avntrainee
"""

import pandas as pd
movie=pd.read_csv("movie_dataset.csv")
#print(movie)

df=pd.DataFrame(movie)
#df.dropna(inplace = True, axis=0)
#df.info()


#Dropping duplicates

df.drop_duplicates(inplace = True)

#Drop column

df.drop(['Description'],inplace=True,axis=1)
#print(df)

#maximum rating

max_rating = df["Rating"].idxmax()
#df.loc[max_rating,'Title']

#What is the average revenue of all movies in the dataset? 

mean_revenue =df["Revenue (Millions)"].mean()
#print(f'Mean revenue = {mean_revenue:.2f} millions')


#What is the average revenue of movies from 2015 to 2017 in the dataset?

#filtered_movies = movie[(movie['Year']>=2015) & (movie['Year']<= 2017)]

#average_revenue_2015_2017 = filtered_movies['Revenue (Millions)'].mean()

#print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_2017}m million dollars")

#How many movies were released in the year 2016

#Count the number of movies released in 2016

#print(df['Year'] == 2016)

#filter_2016 = df['Year'] == 2016

#print(len(df[filter_2016]))

#How many movies were released in the year 2016?

#movie_nolan = df[df["Director"]=="Christopher Nolan"]
#print(len(movie_nolan))

#How many movies in the dataset have a rating of at least 8.0?

# Count the number of movies with a rating of at least 8.0
#high_rated_movies = df[df['Rating'] >= 8.0]

# Output the count
#number_of_high_rated_movies = len(high_rated_movies)
#print(f'Number of movies with a Rating of at least 8.0: {number_of_high_rated_movies}')

#What is the median rating of movies directed by Christopher Nolan?

#nolan_movies = df[df['Director'] == 'Christopher Nolan']

#median_rating = nolan_movies['Rating'].median()


#print(f'median rating of movies directed by Christopher Nolan: {median_rating}')


#Find the year with the highest average rating?


#average_ratings = df.groupby('Year')['Rating'].mean()

#highest_average_year = average_ratings.idxmax()
#highest_average_rating = average_ratings.max()

#print(f'The year with the highest average rating is {highest_average_year} with an average rating of {highest_average_rating:.2f}.')





#What is the percentage increase in number of movies made between 2006 and 2016?



#count_2006 = df[df['Year'] == 2006].shape[0]
#count_2016 = df[df['Year'] == 2016].shape[0]

count_2006 = 0
count_2016 = 0
if count_2006 > 0:
    percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
else:
     percentage_increase = float('inf')


#print(f'Number of movies in 2006: {count_2006}')
#print(f'Number of movies in 2016: {count_2016}')
#print(f'Percentage increase in number of movies made between 2006 and 2016: {percentage_increase:.2f}%'





#actors_series = df['Actors'].dropna()


#all_actors = actors_series.str.cat(sep=',').split(',')


#all_actors = [actor.strip() for actor in all_actors]


#most_common_actor = max(set(all_actors), key=all_actors.count)
#most_common_count = all_actors.count(most_common_actor)


#print(f'The most common actor is: {most_common_actor} with {most_common_count} appearances.')


genres_series = df['Genre'].dropna()

all_genres = genres_series.str.cat(sep=',').split(',')


unique_genres = {genre.strip() for genre in all_genres}

num_unique_genres = len(unique_genres)

print(f'There are {num_unique_genres} unique genres in the dataset.')

