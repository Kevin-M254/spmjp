-- Lists all leagues in spmjp database
SELECT leagues.id, leagues.name, countries.name FROM leagues
INNER JOIN countries ON leagues.country_id = countries.id;
