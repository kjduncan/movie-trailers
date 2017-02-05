# import webbrowser python module to enable opening of webbrowser
import webbrowser


# defining class Movie
class Movie():
    def__init__(self, movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url =
                poster_image
                self.trailer_youtube_url
                = trailer_youtube
# open trailer in new window

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
