#!/usr/bin/env python

"""
Class Movie encapsulates the movie's title, storyline, poster image url and youtube trailer so it can be accessed
by fresh_tomatoes.py to construct a website of movie trailers.
"""

__author__ = 'minhlongdo'

import webbrowser


class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Construct a movie object that contains the movie's title, storyline, URL of poster's image and trailer.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens URL of the trailer on youtube.
        :return: None
        """
        webbrowser.open(self.trailer_youtube_url)
