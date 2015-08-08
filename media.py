# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:30:21 2015

@author: me
"""
import webbrowser

class Movie():
    def __init__(self, title, storyline, poster, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        '''
        A function that opens the default browser and plays the movie trailer
        '''
        webbrowser.open(self.trailer_youtube_url)