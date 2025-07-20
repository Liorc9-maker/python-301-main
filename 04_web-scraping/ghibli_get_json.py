import json
import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
data = response.json()

with open("films.json", "w") as fout:
    json.dump(data, fout)

