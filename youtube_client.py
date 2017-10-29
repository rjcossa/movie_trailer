"""
Description: Youtube Client script used to collect the movie trailer information
using the Youtube Data API

WARNING: Must supply a valid API Key check installation instructions for procedure
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google Developer Console API Key
DEVELOPER_KEY = "API_KEY_VALUE"

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


"""
INPUT: Movie Search String
OUTPUT: YOUTUBE URL 
DESCRIPTION: Generates the Youtube Trailer URL based on the Movie Name
"""


def youtube_search(search_string):

    # Build the Youtube object based on the configuration settings

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=search_string,
        type="video",
        part="snippet",
        maxResults=1
    ).execute()

    # Return the Youtube URL based on the Youtube API Response
    return build_youtube_url(search_response.get("items", [])[0]["id"]["videoId"])


"""
INPUT: Movie Search String
OUTPUT: YOUTUBE URL 
DESCRIPTION: Generates the Youtube Trailer URL based on the Movie Name and returns ERROR_FOUND
if any errors occur
"""


def find_movie(query):
    try:
        return youtube_search(query)
    except HttpError:
        return "ERROR_FOUND"


"""
INPUT: Youtube Video ID
OUTPUT: Youtube Video URL
DESCRIPTION: Builds the Youtube Video URL based on the Video's ID
"""


def build_youtube_url(video_id):
    return "https://www.youtube.com/watch?v="+video_id
