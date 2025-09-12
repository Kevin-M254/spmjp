SELECT matches.match_id, teams.name
FROM matches
INNER JOIN teams ON matches.home_team = teams.id;

SELECT teams.name FROM matches
INNER JOIN teams ON matches.away_team = teams.id;
