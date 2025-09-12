#!/usr/bin/python3
""" Test get() and count() methods """
from models import storage
from models.country import Country
from models.league import League

print("All objects: {}".format(storage.count()))
print("Country objects: {}".format(storage.count(Country)))
print("League objects: {}".format(storage.count(League)))

first_country_id = list(storage.all(Country).values())[0].id
print("First country: {}".format(storage.get(Country, first_country_id)))

first_league_id = list(storage.all(League).values())[0].id
print("First league: {}".format(storage.get(League, first_league_id)))
