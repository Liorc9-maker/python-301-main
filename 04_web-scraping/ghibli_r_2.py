import json

# Load the JSON file
with open("films.json", "r", encoding="utf-8") as fin:
    data = json.load(fin)

# Extract the list of films (assuming structure is {"data": {"films": [...]}})
films = data["data"]["films"]

# Filter films that have a valid running_time (as digit)
valid_films = [
    {**film, "running_time": int(film["running_time"])}
    for film in films
    if "running_time" in film and film["running_time"].isdigit()
]

# Find the longest film manually (without using lambda or max())
longest_film = None
for film in valid_films:
    if longest_film is None or film["running_time"] > longest_film["running_time"]:
        longest_film = film

# Print the result
if longest_film:
    print(f"🎬 Longest Film: {longest_film['title']}")
    print(f"🕒 Running Time: {longest_film['running_time']} minutes")
    print(f"🗓️ Released: {longest_film['release_date']}")
    print(f"🈸 Original Title: {longest_film['original_title']}")
else:
    print("No valid films with running time found.")
