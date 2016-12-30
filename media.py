import webbrowser

# Define the movie class
class Movie():
  """ This class provides a way to store movie related information"""

  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    
    # Create instance variables and assign value
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  # Define an instance method
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
