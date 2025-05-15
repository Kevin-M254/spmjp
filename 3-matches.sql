-- Creates database spmjp with table mjp_matches
CREATE DATABASE IF NOT EXISTS `spmjp`;
CREATE TABLE IF NOT EXISTS `spmjp`.`mjp-01-02-25` (
	PRIMARY KEY(`id`),
	`id`	    INT 		NOT NULL AUTO_INCREMENT,
	`league_id` INT			NOT NULL,
	`match`     VARCHAR(256) NOT NULL,
	`ht_odds`   FLOAT,
	`x_odds`    FLOAT,
	`at_odds`   FLOAT,
	`results`   VARCHAR(256),
	FOREIGN KEY(`league_id`)
	REFERENCES `spmjp`.`leagues`(`id`)
);
