"""
Description: The Movie Database client script used to collect the movie information
based on the movie's name
WARNING: Must supply a valid API Key check installation instructions for procedure

Methods:

request_movie_info(movie_name) - Collect The Movie Information by supplying the movie_name
get_movie_title(movie_info) - Return the Movie Title
get_movie_overview(movie_info) - Return the Movie Storyline
get_movie_url(movie_info) - Return the movie's poster URL
collect_image_url(poster_path) - Return the movie's poster url after being supplied with the poster path
"""

import requests
import json


API_KEY = "API_KEY_VALUE"

# The Movie Database's base API URL
base_url = "https://api.themoviedb.org/3/search/movie?api_key="+API_KEY+"&query="

"""
INPUT: Movie Name
OUTPUT: Movie JSON Information
DESCRIPTION: Fetches the Movie Information from the API 
"""


def request_movie_info(movie_name):
    payload = "{}"
    # Perform HTTP Request and return the JSON Response
    response = requests.request("GET", base_url+movie_name, data=payload)

    # Parse the JSON Information returned from the server

    if "total_results" in response.text:
        json_resp = json.loads(response.text)
        # Return the JSON Information of the movie if any movie's are found
        if json_resp['total_results'] >= 1:
            return json_resp['results'][0]
        else:
            # Return an Invalid Response if no movie's matching the criteria are found
            return "NOT_FOUND"
    else:
        return "ERROR_FOUND"

"""
INPUT: Movie JSON Information
OUTPUT: Movie Title
DESCRIPTION: Returns the Movie Title 
"""


def get_movie_title(movie_info):
    return movie_info['title']


"""
INPUT: Movie JSON Information
OUTPUT: Movie Overview/Storyline
DESCRIPTION: Returns the Movie Story Line
"""


def get_movie_overview(movie_info):
    return movie_info['overview']


"""
INPUT: Movie JSON Information
OUTPUT: Movie Image URL
DESCRIPTION: Returns the Movie Image URL
"""


def get_movie_url(movie_info):
    return collect_image_url(movie_info['poster_path'])


"""
INPUT: Image Relative Path
OUTPUT: Full Image URL
DESCRIPTION: Returns the full image URL from the Image's relative path 
"""


def collect_image_url(poster_path):
    return "https://image.tmdb.org/t/p/w500"+poster_path
