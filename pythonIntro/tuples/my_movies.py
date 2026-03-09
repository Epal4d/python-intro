#Create a LIST where each element is a TUPLES
movie_collection = [
    ("The Godfather", "Francis Ford Coppola", 1972),
    ("Inception", "Christopher Nolan",2010),
    ("Parasite", "Bong Joon-ho", 2019),
    ("Goodfellas","Martin Scorsese", 1990),
    ("The Dark Knight", "Christopher Nolan", 2008)
]
#Function to add a new movie
def add_movies(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"Movie: {title} has been added to collection")

#Function to display all movies in collection
def display_movies():
    print(f"Movie Collection:")
    for title, director, year in movie_collection:
        print(f"Title: {title}, Director: {director}, Release Year: {year}")

def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director


movies_by_scorsese = search_by_director("Martin Scorsese")
print(f"Books by Scorsese")
for title, director, year in movies_by_scorsese:
    print(f"Title: {title}, Release Year:{year}")



display_movies()
print(movies_by_scorsese)

