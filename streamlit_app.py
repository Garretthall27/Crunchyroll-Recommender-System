# import streamlit and other libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# load in the csv files for the recommender system
model_df = pd.read_csv('./Data/model_df.csv', index_col='jw_entity_id')
lookup_table = pd.read_csv('./Data/lookup_table.csv', index_col='jw_entity_id')
# change column types from float to int
lookup_table['release_year'] = lookup_table['release_year'].astype(int)
lookup_table['seasons'] = lookup_table['seasons'].astype(int)
# chanege column names to more presentable names
lookup_table.columns = ['Title', 'Type', 'Year Released', 'Seasons']

# create the recommender system function
# Creating cosine recommendation function
def preference_cosine_rec(model_df, title, num_recs, type_pref, genre_pref):
    '''
    This function will return a number of recommendations based off 
    the title and number of recommendations the user inputs.
    '''

    # Filtering model_df based on type_pref
    if type_pref == 'Show':
        filtered_model_df = model_df.loc[model_df['show_'] == 1]
    elif type_pref == 'Movie':
        filtered_model_df = model_df.loc[model_df['movie_'] == 1]
    else:
        filtered_model_df = model_df
  
    # Filtering filtered_model_df by genre
    if genre_pref == 'No Preference':
        filtered_model_df = filtered_model_df
    else:
        filtered_model_df = filtered_model_df.loc[filtered_model_df[genre_pref] == 1]

    # Get the index of the row for the title
    title_index = lookup_table.index[lookup_table['Title'] == title]
    # get the row of the title_index from model_df and reshape it
    title_array = np.array(model_df.loc[title_index]).reshape(1,-1)

    # check if title_index is in filtered_model_df
    # Append the title array to the filtered_model_df if it is not
    if title_index not in list(filtered_model_df.index):
        filtered_model_df = filtered_model_df.append(model_df.loc[title_index])
   

    # Create the cosine similarity matrix based on the title
    # cosine similarity matrix
    cosine_matrix = cosine_similarity(filtered_model_df, title_array)

    # create a dataframe from the cosine_matrix
    cosine_df = pd.DataFrame(data=cosine_matrix, index=filtered_model_df.index)

    # top n results of the cosine_df
    results = cosine_df.sort_values(0, ascending=False).index.values[:num_recs+1]
    
    # look up values in look up table and return the table
    return lookup_table.loc[results][1:]


# the function is created for the recommender system
# Below code is for designing and implementing streamlit

# Make streamlit wider
st.set_page_config(layout="centered")

# Image of Crunchyroll logo
st.image('./Images/Crunchyroll-logo.jpg')

# Title of the page
st.write('# Anime Recommender App')

# Summary of the app
st.write('This app will give you anime recommendations that are similar to an anime you choose. \
    Choose an anime from our list of shows and movies below and choose how many \
    recommendations you would like. You can also choose if you want only movies, shows, \
    or either returned. There is also an option to only recommend anime of a certain genre.')

# Get the inputs for the recommender system

# Get list of titles for searching
list_of_titles = ['Type in a show or movie']
list_of_titles.extend(lookup_table['Title'])
# Search bar for the titles
title = st.selectbox("Select a show or movie you want a recommendation for: ", list_of_titles)

# Get number of recommendations
range_of_recs = range(1,11)
num_recs = st.selectbox("How many recommendations would you like?", range_of_recs)

# Get type of show
type_list = ['No Preference', 'Show', 'Movie']
type_pref = st.selectbox("Do you have a preference on the type of recommendation?", type_list)

# Get the genre preference
genre_list = ['No Preference']
genre_list.extend(list(model_df.columns)[504:-2])
genre_pref = st.selectbox("Do you have a preference for a genre?", genre_list)

# Button to activate recommender function
rec_button = st.button("Give Me Recommendations!")

if rec_button:
    # Run the function and assign it to df
    df = preference_cosine_rec(model_df, title, num_recs, type_pref, genre_pref)
    
    # The below code will output the df without the index column
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
        <style>
        .row_heading.level0 {display:none}
        .blank {display:none}
        </style>
        """

    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Display an interactive table
    st.table(df)
