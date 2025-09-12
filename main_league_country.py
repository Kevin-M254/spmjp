#!/usr/bin/python3
""" Test leagues access from a Country """
from models import storage
from models.country import Country
from models.league import League

""" Object creation """
country_1 = Country(name="Italy")
print("New country: {}".format(country_1))
country_1.save()

country_2 = Country(name="Spain")
print("New country: {}".format(country_2))
country_2.save()

league_1_1 = League(country_id=country_1.id, name="Serie_A")
print("New league: {} in the country {}".format(league_1_1, country_1))
league_1_1.save()
league_1_2 = League(country_id=country_1.id, name="Serie_B")
print("New league: {} in the country {}".format(league_1_2, country_1))
league_1_2.save()
league_2_1 = League(country_id=country_2.id, name="La_Liga")
print("New league: {} in the country {}".format(league_2_1, country_2))
league_2_1.save()

""" Verification """
print("")
all_countries = storage.all(Country)
for country_id, country in all_countries.items():
    for league in country.leagues:
        print("Find league {} in country {}".format(league, country))
