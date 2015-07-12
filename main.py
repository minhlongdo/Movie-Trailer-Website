import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://www.filmandtvnow.com/wp-content/uploads/2014/11/Toy-Story-Characters1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movie.Movie("Avatar", "A marine on an alien planet",
                     "http://smellslikescreenspirit.com/wp-content/uploads/2009/08/AvatarTeaserPoster-460x687.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

ratatouille = movie.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = movie.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = movie.Movie("Hunger Games", "A really real reality show",
                           "https://musicmoviesthoughts.files.wordpress.com/2013/04/hunger-games.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
