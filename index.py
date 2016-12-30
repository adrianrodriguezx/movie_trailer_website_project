import media
import fresh_tomatoes

# Inception
incenption = media.Movie("Inception",
	"A professional thief who steals information by infiltrating people's dreams",
	"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=8hP9D6kZseM")

# Siete Viergenes
siete_virgenes = media.Movie("7 Virgenes",
	"A teenager is given a 48 hour leave from a juvenile reform center to attend his brother weeding",
	"http://pics.filmaffinity.com/7_virgenes-483661126-large.jpg",
	"https://www.youtube.com/watch?v=29txqk7I-0U")

# Interstellar
interstellar = media.Movie("Interstellar", 
	"Astronauts travel through a wormhole in search of a new home for humanity", 
	"http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB", 
	"https://www.youtube.com/watch?v=SIZpLFPQLLg")

# Y Tu Mama Tambien
y_tu_mama_tambien = media.Movie("Y Tu Mama Tambien",
	"A story about two teenage boys who take a road trip with a woman in her late twenties", 
	"https://upload.wikimedia.org/wikipedia/en/6/63/Y_tu_mam%C3%A1_tambi%C3%A9n_poster.png",
	"https://www.youtube.com/watch?v=pdh8Va2oDKk")

# Ex Machina
ex_machina = media.Movie("Ex Machina",
	"A progammer test a humanoid robot if is capable of though and consciousness",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
	"https://www.youtube.com/watch?v=bggUmgeMCdc")

# Victoria
victoria = media.Movie("Victoria",
	"A young Spanish woman who has newly moved to Berlin finds her flirtation with a local guy turn potentially deadly as their night out with his friends reveals a dangerous secret",
	"https://upload.wikimedia.org/wikipedia/en/f/fe/Victoria_%282015_film%29_POSTER.jpg",
	"https://www.youtube.com/watch?v=Kp8wcV3GjW0")

# Create a list of movies
movies = [incenption, siete_virgenes, interstellar, y_tu_mama_tambien, ex_machina, victoria]

# Generate web page 
fresh_tomatoes.open_movies_page(movies)
