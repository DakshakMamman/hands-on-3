"""
Task 2: Film Night Prep
You're helping your community plan a Friday Film Night for kids. The initial list of movie genres to be shown includes:
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

1. Add the genre "Drama" at the end of the list because parents requested it.
2. Someone mistakenly added "Fantasy" twice. Make sure there's only one "Fantasy" in the list.
3. The organizer wants to know how many genres are now planned to be shown.
4. Display the second and second-to-last genres to verify diversity.

→ Modify the list and display the required results.
"""
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

genres.append("Drama")

genres.remove("Fantasy")  
genres.insert(3, "Fantasy")  

total_genres = len(genres)

second_genre = genres[1]
second_last_genre = genres[-2]
print("Total Genres:", total_genres)
print("Second Genre:", second_genre)
print("Second-to-Last Genre:", second_last_genre)

