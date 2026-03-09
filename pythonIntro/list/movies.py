# Initialization of empty list 
favorite_movies = []

# Function to add a movie
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"movie '{movie}' added.")

# Function to remove a movie
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else: print (f"movie '{movie}' not found.")

# function to display all favorite movies
def display_movies():
    print("Favorite movies List:")
    for movie in favorite_movies:
        print(f"- {movie}")

# Adding movies
add_movie("Hitch")
add_movie("Coming to America")
add_movie("Beverly Hills Cop")
add_movie("The Wiz")


# Display Movie
display_movies()

#Remove a movie
remove_movie("The Wiz")

#Displaying movie again 
display_movies()