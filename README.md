![image](https://user-images.githubusercontent.com/108245743/193600594-46ac3a05-1cbd-4644-a47c-2b4f08fa7b50.png)
# Crunchyroll Recommender System - Content Based Approach

## Project Overview

Sony Pictures Entertainment, the company that owns Funimation, has purchased Cunchyroll roll this year and plans on moving its content from Funimation to Crunchyroll. Funimation users will eventually have to acquire a Crunchyroll subscription to continue watching their favorite anime. This is a great opportunity for Crunchyroll to implement a new content based recommendation system. The goal of this project is to create a content based recommendation system and deploy it through a web application hosted by Streamlit using the anime titles from Crunchyroll and Funimation. I created a content based recommendation system using cosine similarity from data I scraped from [justwatch.com](https://www.justwatch.com/). This repository contains two jupyter notebooks. The [JustWatch_scraping.ipynb](https://github.com/Garretthall27/Recommender-System/blob/main/JustWatch_scraping.ipynb) notebook contains the code for scraping and collecting the data from justwatch.com. The [Recommender_system_workflow.ipynb](https://github.com/Garretthall27/Recommender-System/blob/main/Project_workflow.ipynb) notebook contains the code for the workflow of the recommender system. This includes data cleaning, preprocessing, creating the recommender system, and evaluation. The GitHub also contains a python file, [streamlit_app.py](https://github.com/Garretthall27/Crunchyroll-Recommender-System/blob/main/streamlit_app.py), which contains the code used for the Streamlit app. The Streamlit app can be found [here](https://garretthall27-crunchyroll-recommender-syst-streamlit-app-ezl87s.streamlitapp.com/).

## Business and Data Understanding

### Business Problem

Crunchyroll and Funimation have been leaders in the anime industry. Providing the best and newest anime show and movies on their respective streaming apps. In 2022, Sony Pictures Entertainment, the company that owns Funimation, acquired Crunchyroll and decided to keep the Crunchyroll brand and move the content from Funimation onto Crunchyroll's streaming platform. This also means Funimation users will eventually have to purchase a Crunchyroll subscription to continue watching their favorite anime. With new content and users coming to their platform, this is a great a opportunity for Crunchyroll to implement a new content based recommendation system. I have created a content based recommendation system for Crunchyroll using the anime titles available on both Crunchyroll and Funimation. The recommendation system uses cosine similarity and has information on each title including genre, synopsis, the movie database score, release year, number of seasons, and runtime. The recommendation system was deployed through a web application I built, hosted on Streamlit [here](https://garretthall27-crunchyroll-recommender-syst-streamlit-app-ezl87s.streamlitapp.com/).

### Data Understanding

The data used was collected by scraping [justwatch.com](https://www.justwatch.com/) using a Just Watch API. The GitHub for the API I used can be found [here](https://github.com/dawoudt/JustWatchAPI). Originally, I was planning on using data already gathered by a GitHub user named Victor Soeiro. His GitHub is located [here](https://github.com/victor-soeiro/WebScraping-Projects) and contains csv files he created by scraping justwatch.com. The csv files on his GitHub included information about each show and title available on Crunchyroll and Funimation. He had gathered this information on his own through justwatch.com and I was planning on using the csv files he had, but after inspecting the csv files I noticed not all the titles were accounted for and there were some missing values. So I decided to scrape the data from justwatch.com myself to make sure I had all the information I needed.

The data I collected on each of the titles from justwatch.com was very similar to the data Victor Soeiro collected on his GitHub. The columns of the dataframe after I collected the information from the API are as follows: `jw_entity_id` `id` `title` `poster` `description` `release_year` `type` `imdb_popularity` `tmdb_popularity` `imdb_score` `imdb_votes` `tmdb_score` `imdb_id` `tmdb_id` `genre_ds` `age_certification` `runtime` `production_countries` `seasons` `streaming_app`. I collected this information from Crunchyroll and Funimation titles and then combined the two into one csv file. The csv file containing all the titles collected through the API can be found in the [Data folder](https://github.com/Garretthall27/Crunchyroll-Recommender-System/tree/main/Data) under the name `titles.csv`. Once data was collected, I moved onto the data cleaning. The data cleaning process consisted of dropping duplicate rows because some titles are on both the Crunchyroll and Funimation streaming apps. From there I handled null values for the genres, descriptions, released year, and the runtimes. There were also titles that shared the same names even though they are different shows/movies. I changed the titles of these shows/movies so they are not longer duplicates.

### Data Preprocessing

To experiment and evaluate the recommender systems, I used two forms of data preprocessing on the dataset. I created two new datasets with a different scaler used on each one. One of the datasets used MinMaxScaler and the other StandardScaler. The purpose of using two different scalers was to experiment with the performance of the recommender systems to see if the outputs of the two datasets would be different. Overall, I did find differences in the recommendations being returned amongst the two datasets, but I found the StandardScaler dataset provider better recommendations for what I was trying to achieve with this project. I also used a TF-IDF Vectorizer on the descriptions of the shows along with the other features to add another layer of similarity in the recommender system.

## Recommendation Systems and Evaluation

### Cosine Similarity and Nearest Neighbors

I created two different recommender systems for this project to evaluate which one is better. One recommender system uses Cosine Similarity while the other uses Nearest Neighbors. I tested these recommender systems on the two datasets mentioned earlier to compare the results of one another. 

### Final Recommendation System - Cosine Similarity

After evaluating all of the recommendation systems, the final recommendation system I created used Cosine Similarity and the dataset that was preprocessed using StandardScaler and TF-IDF Vectorizer. The recommendation system uses cosine similarity to find the most similar shows and movies to the title that was inputted. The features used in this system are the movie database score, the year the title was released, runtime, the number of seasons, genre, and description. The recommendation system also has two additional user preference inputs which allow users to enter the type of content they want (show or movie) and a specific genre. For example, the user can enter  “Naruto” and “Comedies” and the app will only return Comedies that are similar to Naruto.

## Web Application

For the final part of the project, I deployed my recommendation system through a web application hosted by Streamlit which can be found [here](https://garretthall27-crunchyroll-recommender-syst-streamlit-app-ezl87s.streamlitapp.com/). The web application is built upon the recommendation system I created and allows users to search and enter a show or movie from the list provided and it will return a number of recommendations that are most similar to the title they entered. The code for the streamlit app can be found in the [streamlit_app.py file](https://github.com/Garretthall27/Crunchyroll-Recommender-System/blob/main/streamlit_app.py) and the requirements needed for Streamlit to host the app can be found in the [requirements.txt file](https://github.com/Garretthall27/Crunchyroll-Recommender-System/blob/main/requirements.txt).

Below is a demonstration of the web application and shows 3 examples of how it can be used. For the first example, I am entering One Piece for the title and 4 recommendations. The output is a table with the title, type of content, the year it was released, and the number of seasons for the shows or movies similar to One Piece. Next it will demonstrate more of the user preferences and enter Attack on Titan, shows, and the Crime genre. You can see from the table it is recommending Crime shows that are most similar to Attack on Titan. Finally, to show more of the user preferences it will enter in Berserk, shows, and Comedies. The application will return Comedies that are most similar to the show Berserk.

[streamlit-streamlit_app-2022-10-04-17-10-01.webm](https://user-images.githubusercontent.com/108245743/194658965-3c52b979-de21-4a72-a029-01bcc520e4f6.webm)

## Conclusion

The goal of this project was to create a content based recommendation system for Crunchyroll using Crunchyroll's library of titles and the new Funimation titles coming to its platform. The recommendation system uses cosine similarity to find the most similar shows and movies to the title the user wants. The recommendation system allows for the users to enter in additional information about the recommendations they want including type of content and genre. Crunchyroll can deploy this application by offering it to new and existing users to give them new shows and movies to consider watching. They can offer the application to users right after they sign up or offer it as a pop up to existing users.

## Repository Structure
```
├── Data
│   ├── lookup_table.csv
│   ├── model_df.csv
│   ├── titles.csv
├── Images
│   ├── Crunchyroll-logo.jpg
├── .gitignore
├── JustWatch_scraping.ipynb
├── README.md
├── Recommendation_system_workflow.ipynb
├── requirements.txt
└── streamlit_app.py
```
