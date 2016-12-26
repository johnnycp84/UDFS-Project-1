import fresh_tomatoes  # Import file that contains website code
import media  # Import file that contains Movie class

# Initiate class Movie and populate class variables for each movie
the_big_lebowski = media.Movie("The Big Lebowski", "The dude abides",
                               "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=cd-go0oBF4Y")

the_life_aquatic = media.Movie("The Life Aquatic", "The Zissou",
                               "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=yh401Rmkq0o")

the_sting = media.Movie("The Sting",
                        "One of the most stylish movies of the year",
                        "https://upload.wikimedia.org/wikipedia/en/9/9c/Stingredfordnewman.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=LN2hBOIXhBs")

the_trip = media.Movie("The Trip", "Eat, Drink and Try Not to Kill Eachother",
                       "https://upload.wikimedia.org/wikipedia/en/8/8f/Trip_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=Xxq-I_e_KXg")

the_italian_job = media.Movie("The Italian Job", "Italian crime caper",
                              "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Italian_Job_1969_poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=FEltJsIwSvE")

the_bounty = media.Movie("The Bounty", "They were friends through hell."
                         "They became enemies in Paradise",
                         "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Bounty.jpg",   # NOQA
                         "https://www.youtube.com/watch?v=g5QER2wu0lg")

# Create movie list
movies = [the_big_lebowski, the_life_aquatic, the_sting, the_trip,
          the_italian_job, the_bounty]

# Open webpage with favourite movies with our movies list as input
fresh_tomatoes.open_movies_page(movies)
