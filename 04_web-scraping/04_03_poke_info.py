# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
import requests
BASE_URL = "https://pokeapi.co/api/v2/"

class Pokemon:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        response = requests.get(f"{BASE_URL}pokemon/{self.name.lower()}")
        if response.status_code == 200:
            data = response.json()
            self.name = data['name']
            self.number = data['id']
            self.types = [t['type']['name'] for t in data['types']]
        else:
            raise Exception(f"Failed to fetch data for {self.name}")
    def __str__(self):
        return f"Name: {self.name.capitalize()} \nNumber: {self.number} \nTypes: {', '.join(self.types)}\n-------\n"


a =Pokemon("pikachu")
a.get_info()
print(a)
b = Pokemon("charmander")
b.get_info()
print(b)
c = Pokemon("bulbasaur")
c.get_info()
print(c)    
d = Pokemon("squirtle")
d.get_info()
print(d)
e = Pokemon("eevee")
e.get_info()
print(e)    
f = Pokemon("jigglypuff")
f.get_info()
print(f)