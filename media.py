import webbrowser


class Movie():
    """Movie is a class to store movie relavant information.

    Attributes:
        title (str): The title of the movie.
        storyline (str): The storyline of the movie.
        poster_image_url (str): The link to the image/poster of the movie.
        trailer_youtube_url (str): The link to the movie's youtube trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits a Movie with attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the web browser using the youtube url."""
        webbrowser.open(self.trailer_youtube_url)
