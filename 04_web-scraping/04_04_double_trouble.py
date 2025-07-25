# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.
import requests

class GhibliFetcher:
    def __init__(self):
        self.species_url = "https://ghibliapi-iansedano.vercel.app/api/species"

    def fetch_species_names(self):
        try:
            response = requests.get(self.species_url)
            response.raise_for_status()
            data = response.json()
            species = data.get("data", {}).get("species", [])

            if not isinstance(species, list):
                print("❌ Unexpected format: 'species' is not a list.")
                return []

            species_names = [s["name"] for s in species if "name" in s]
            print("✅ Species fetched:", species_names)
            return species_names

        except Exception as e:
            print(f"❌ Failed to parse species JSON: {e}")
            return []

class PokemonFetcher:
    def __init__(self, type_url):
        self.type_url = type_url

    def fetch_pokemon_names(self):
        try:
            response = requests.get(self.type_url)
            response.raise_for_status()
            data = response.json()
            pokemon_list = [p["pokemon"]["name"] for p in data["pokemon"]]
            print("✅ Pokémon fetched:", pokemon_list[:5])
            return pokemon_list
        except Exception as e:
            print(f"❌ Failed to fetch Pokémon: {e}")
            return []

class MashupDisplay:
    def __init__(self, species_list, pokemon_list):
        self.species = species_list
        self.pokemon = pokemon_list

    def display(self):
        if not self.species or not self.pokemon:
            return "❌ Could not load data properly."

        result = "✨ Ghibli x Pokémon Mashup ✨\n"
        for i, sp in enumerate(self.species[:5]):
            poke = self.pokemon[i % len(self.pokemon)]
            result += f"- {sp} pairs with Pokémon: {poke}\n"
        return result

if __name__ == "__main__":
    ghibli = GhibliFetcher()
    poke_type_url = "https://pokeapi.co/api/v2/type/ghost"
    pokemon = PokemonFetcher(poke_type_url)

    species = ghibli.fetch_species_names()
    pokemons = pokemon.fetch_pokemon_names()

    mashup = MashupDisplay(species, pokemons)
    print(mashup.display())
