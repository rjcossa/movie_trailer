"""
----------------
Movie Class
----------------

Attributes:
title - Movie Title
storyline - Movie Storyline
poster_image_url - Movie's poster URL
trailer_youtube_url - Movie's Youtube URL


Methods:
show_trailer - Used to open a browser and display the Movie's Information

"""

import webbrowser

class Movie:

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
