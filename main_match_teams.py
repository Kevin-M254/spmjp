#!/usr/bin/python3
""" Test link Many-To-Many Match <> Team """
from models import *
from models.country import Country

# Creation of Country
country = Country(name="Kenya")
country.save()

# Creation of League
league = League(country_id=country.id, name="KPL")
league.save()

# Creation of two Matches
match_1 = Match(league_id=league.id, home_team="team_1", away_team="team_2")
match_1.save()

match_2 = Match(league_id=league.id, home_team="team_3", away_team="team_2")
match_2.save()

# Creation of 3 Various Team
team_1 = Team(name="Gor")
team_1.save()
team_2 = Team(name="Leopards")
team_2.save()
team_3 = Team(name="Bandari")
team_3.save()

#link match_1 with 2 teams
match_1.teams.append(team_1)
match_1.teams.append(team_2)

#link match_2 with 2 teams
match_2.teams.append(team_2)
match_2.teams.append(team_3)

storage.save()

print("OK")
