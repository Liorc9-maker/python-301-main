animals_of_africa = {
    "aardvark": "a nocturnal badger-sized burrowing mammal",
    "zebra": "a wild horse with black-and-white stripes"
    }

animal = input("Animal to look up: ")

print(animals_of_africa.get(animal, "This animal is not in the database"))
