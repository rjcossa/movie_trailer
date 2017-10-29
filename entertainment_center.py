"""

----------------
Entertainment Center
----------------

Python Script that generates a list of objects of the movie class
based on the movie name and creates an html file based on the input


Methods:

create_movie(result) - Takes in the Movie JSON Information and creates a movie object

"""
import youtube_client
import media
import tmdb_client
import fresh_tomatoes

# Initialization of the movie list
movies = []

"""
INPUT: JSON String containing movie information
Description: Function that creates a movie object after receiving the JSON movie Information
"""


def create_movie(result):

    # Collect Information to create the movie
    title = tmdb_client.get_movie_title(result)
    youtube_link = youtube_client.find_movie(title + " Trailer")
    storyline = tmdb_client.get_movie_overview(result)
    poster_url = tmdb_client.get_movie_url(result)

    # Create the movie object
    new_movie = media.Movie(title, storyline, poster_url, youtube_link)

    # Add the movie object to the movie list
    movies.append(new_movie)


# Get the movie name list from the movie_list.txt file
movie_list = [line.rstrip('\n') for line in open('movie_list.txt')]

# Loop through the list of movies and create the movie objects
for movie in movie_list:

    # Get the movie information from the TMDB Movie API
    res = tmdb_client.request_movie_info(movie)
    if res != "NOT_FOUND":
        create_movie(res)

# Create the Movie HTML File from the list of Movies
fresh_tomatoes.open_movies_page(movies)
