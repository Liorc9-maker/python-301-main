import json

with open("films.json", "r") as fin:
    data = json.load(fin)



# Navigate to the list of films
films = data["data"]["films"]

# Print each film's title and director
for film in films:
    title = film.get("title", "Unknown Title")
    director = film.get("director", "Unknown Director")
    print(f"{title} — directed by {director}")