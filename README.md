![image](https://user-images.githubusercontent.com/108245743/193600594-46ac3a05-1cbd-4644-a47c-2b4f08fa7b50.png)
# Crunchyroll Recommender System - Content Based Approach

## Project Overview

Sony Pictures Entertainment, the company that owns Funimation, has purchased Cunchyroll roll this year. Sony plans on moving its content from Funimation to Crunchyroll, and Funimation users will have to acquire a Crunchyroll subscription to watch their favorite anime. This is a great opportunity for Crunchyroll to implement a new content based recommendation system. The goal of this project is to create a content based recommendation system using the anime titles from Crunchyroll and Funimation. I created a content based recommendation system using cosine similarity from data I scraped from [justwatch.com](https://www.justwatch.com/). This repository contains two jupyter notebooks. The [JustWatch_scraping.ipynb](https://github.com/Garretthall27/Recommender-System/blob/main/JustWatch_scraping.ipynb) notebook contains the code for scraping and collecting the data from justwatch.com. The [Project_workflow.ipynb](https://github.com/Garretthall27/Recommender-System/blob/main/Project_workflow.ipynb) notebook contains the code for the workflow of the recommender system. This includes data cleaning, preprocessing, creating the recommender system, and evaluation.

## Business and Data Understanding

### Business Problem

Crunchyroll and Funimation have been leaders in the anime industry. Providing the best and newest anime show and movies on their respective streaming apps. In 2022, Sony Pictures Entertainment, the company that owns Funimation, acquired Crunchyroll and decided to keep the Crunchyroll brand and move the content from Funimation onto Crunchyroll's streaming platform. This also means Funimation users will eventually have to purchase a Crunchyroll subscription to continue watching their favorite anime. With new content and users coming to their platform, this is a great a opportunity for Crunchyroll to implement a new content based recommendation system. I have created a content based recommendation system for Crunchyroll using the anime titles available on both Crunchyroll and Funimation. The recommendation system uses cosine similarity and has information on each title including genre, synopsis, the movie database score, release year, number of seasons, and runtime.

### Data Understanding

The data used was collected by scraping [justwatch.com](https://www.justwatch.com/) using a Just Watch API. The GitHub for the API I used can be found [here](https://github.com/dawoudt/JustWatchAPI). Originally, I was planning on using data already gathered by a GitHub user named Victor Soeiro. His GitHub is located [here](https://github.com/victor-soeiro/WebScraping-Projects) and contains csv files he created by scraping justwatch.com. He had gathered this information on his own through justwatch.com and I was planning on using the csv files he had, but after inspecting the csv files I noticed not all the titles were accounted for and there were some missing values. So I decided to scrape the data from justwatch.com myself to make sure I had all the information I needed.

The data I collected on each of the titles from justwatch.com was very similar to the data Victor Soeiro collected on his GitHub. The columns of the dataframe after I collected the information from the API are as follows: `jw_entity_id` `id` `title` `poster` `description` `release_year` `type` `imdb_popularity` `tmdb_popularity` `imdb_score` `imdb_votes` `tmdb_score` `imdb_id` `tmdb_id` `genre_ds` `age_certification` `runtime` `production_countries` `seasons` `streaming_app`. I collected this information from Crunchyroll and Funimation titles and then combined the two into one csv file. Once data was collected, I moved onto the data cleaning. The data cleaning process consisted of dropping duplicate rows because some titles are on both the Crunchyroll and Funimation streaming apps. From there I handled null values for the genres, descriptions, and the runtimes. There were also titles that shared the same names even though they are different shows/movies. I changed the titles of these shows/movies so they are not longer duplicates.



## Recommendation Systems and Evaluation

### Final Recommendation System - Cosine Similarity

## Conclusion

