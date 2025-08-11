from collections import namedtuple

Geolocation = namedtuple("geolocation", "name lat lon")
null_island = Geolocation(name="Null Island", lat=0 , lon=0)
print(null_island[0])
print(null_island.name)

maccu_piccu = Geolocation(name="Maccu Piccu", lat=-13.163108055193145, lon=-72.54496539348477)
maccu_piccu_tuple = ("Maccu Piccu", -13.163108055193145, 72.54496539348477)

# Get the latitude from the plain tuple
print(maccu_piccu_tuple[1])  # -13.163108055193145 - Wait... or was it at index 0? Or index 2? Arrgh!

# Get the latitude from the namedtuple
print(maccu_piccu.lat)  # -13.163108055193145 - Yay!

null_island_dict = null_island._asdict()
null_island_dict["name"] = "Null Island is not an island"

modified_null_island = Geolocation(**null_island_dict)
print(modified_null_island)  # Geolocation(name='Null Island is not an island', lat=0, lon=0)
