# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:38:31 2015

@author: me
"""

import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A Story about a boy and his toys',
                        'http://parkwaynews.net/corral/wp-content/uploads/2014/04/Toy-Story-Poster.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
                        
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A paralyzed former Marine, falls in love and is drawn into a battle for the survival of Pandora.",
                     "http://www.overthinkingit.com/wp-content/uploads/2009/12/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# avatar.show_trailer()

menofh = media.Movie('Men of Honour',
                     "The story of Carl Brashear, the first African American, then also the first amputee, US Navy Diver and the man who trained him.",
                     'https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Men_of_honor_ver1.jpg/220px-Men_of_honor_ver1.jpg',
                     'https://www.youtube.com/watch?v=Up_xZ0VOSUM')
# menofh.show_trailer()

rambo1 = media.Movie('RAMBO: First Blood',
                     "A Vietnam Veteran uses his combat skills against the lawman of a small town when they arrest and abuse him.",
                     'https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/First_blood_poster.jpg/220px-First_blood_poster.jpg',
                     'https://www.youtube.com/watch?v=rjptQSfuTy8')
# rambo1.show_trailer()

rambo2 = media.Movie('RAMBO: First Blood P2',
                     "John Rambo is released from prison by the government for a top-secret covert mission to the jungles of Vietnam.",
                     'https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Rambo_first_blood_part_ii.jpg/220px-Rambo_first_blood_part_ii.jpg',
                     'https://www.youtube.com/watch?v=WQGJAIYtWD4')
# rambo2.show_trailer()

intouchables = media.Movie('The Intouchables',
                     "After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.",
                     'https://upload.wikimedia.org/wikipedia/en/thumb/9/93/The_Intouchables.jpg/220px-The_Intouchables.jpg',
                     'https://www.youtube.com/watch?v=R8wUIez--WE')

# intouchables.show_trailer()
movies = [menofh, intouchables, avatar, toy_story, rambo1, rambo2]
fresh_tomatoes.open_movies_page(movies)
