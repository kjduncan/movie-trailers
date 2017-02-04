import fresh_tomatoes
import media

up = media.Movie("UP", "Two unusual friends go on an amazing adventure",
                 "http://www.impawards.com/2009/posters/up.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

#print(up.storyline)
space_odyssey = media.Movie("2001:A Space Odyssey",
                     "An exploration of space and the woes of AI",
                     "http://www.fatmovieguy.com/wp-content/uploads/2014/12/2001-A-Space-Odyssey-Movie-Poster.png",
                     "https://www.youtube.com/watch?v=Ok32VyEQYYc")
#print(2001_space_odyssey.storyline)
#2001_space_odyssey.show_trailer()

forrest_gump = media.Movie("Forrest Gump",
                           "The story of a man's life",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcQCFOcMb5_zkdZg4B4JvIGLlTQTvLdtLjiS5axJJDqP1FaI8Yyx",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")
#print(forrest_gump.storyline)
#forrest_gump.show_trailer()
youve_got_mail = media.Movie("You've Got Mail", "Love in the age of technology",
                             "https://images-na.ssl-images-amazon.com/images/I/51Fas4vPGcL._AC_UL320_SR214,320_.jpg",
                             "https://www.youtube.com/watch?v=znESQTt3L80")
the_good_dinosaur = media.Movie("The Good Dinosaur", "A dinosaur finding his way home",
                          "http://www.impawards.com/2015/posters/good_dinosaur_ver3_xlg.jpg",
                          "https://www.youtube.com/watch?v=7BrH72aFXfI")
ghost_town = media.Movie("Ghost Town", "A dentist gets caught up in unfinished business",
                                "http://www.impawards.com/2008/posters/ghost_town.jpg",
                                "https://www.youtube.com/watch?v=oUul8PD_CGo")


movies= [up, space_odyssey, forrest_gump, youve_got_mail, the_good_dinosaur, ghost_town]
fresh_tomatoes.open_movies_page(movies)
