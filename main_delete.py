#!/usr/bin/python3
""" Test delete feature """
from models.engine.file_storage import FileStorage
from models.country import Country

fs = FileStorage()

# All Countries
all_countries = fs.all(Country)
print("All Countries: {}".format(len(all_countries.keys())))
for country_key in all_countries.keys():
    print(all_countries[country_key])

# Create new Country
new_country = Country()
new_country.name = "Portugal"
fs.new(new_country)
fs.save()
print("New Country: {}".format(new_country))

# All Countries
all_countries = fs.all(Country)
print("All Countries: {}".format(len(all_countries.keys())))
for country_key in all_countries.keys():
    print(all_countries[country_key])

# Create another Country
another_country = Country()
another_country.name = "Italy"
fs.new(another_country)
fs.save()
print("Another Country: {}".format(another_country))

# All Countries
all_countries = fs.all(Country)
print("All Countries: {}".format(len(all_countries.keys())))
for country_key in all_countries.keys():
    print(all_countries[country_key])

# Delete the new Country
fs.delete(new_country)

# All Countries
all_countries = fs.all(Country)
print("All Countries: {}".format(len(all_countries.keys())))
for country_key in all_countries.keys():
    print(all_countries[country_key])
