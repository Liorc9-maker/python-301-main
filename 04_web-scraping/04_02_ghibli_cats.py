# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

#BASE_URL = "https://ghibliapi-iansedano.vercel.app"
import requests

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

# Step 1: Get all species
species_url = f"{BASE_URL}/api/species"
species_response = requests.get(species_url)

if species_response.status_code != 200:
    print("Failed to fetch species")
    exit()

species_data = species_response.json()

# Step 2: Find the species ID for 'Cat'
cat_species = [s for s in species_data["data"]["species"] if "cat" in s["name"].lower()]

if not cat_species:
    print("No cat species found")
    exit()

for cat in cat_species:
    print(f"Species: {cat['name']}")
    print(f"Classification: {cat.get('classification', 'N/A')}")
    print(f"Eye colors: {cat.get('eye_colors', 'N/A')}")
    print(f"Hair colors: {cat.get('hair_colors', 'N/A')}")
    print("-----")

    # Step 3: Get characters of this species
    cat_species_id = cat["id"]
    people_url = f"{BASE_URL}/api/people"
    people_response = requests.get(people_url)

    if people_response.status_code != 200:
        print("Failed to fetch people")
        exit()

    people_data = people_response.json()
    cat_characters = [
        p for p in people_data["data"]["people"]
        if p["species"].endswith(f"/{cat_species_id}")
    ]

    if not cat_characters:
        print("No cat characters found.")
        continue

    for character in cat_characters:
        print(f"Name: {character['name']}")
        print(f"Gender: {character.get('gender', 'Unknown')}")
        print(f"Age: {character.get('age', 'Unknown')}")

        # Step 4: Get film info
        for film_url in character["films"]:
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film = film_response.json()
                film_data_list = film.get("data", [])
                if film_data_list:
                    film_data = film_data_list[0]
                    print(f"Appears in: {film_data['title']} ({film_data['release_date']})")

        print("-----")
