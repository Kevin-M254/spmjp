-- Creates database spmjp with the table leagues
CREATE DATABASE IF NOT EXISTS `spmjp`;
CREATE TABLE IF NOT EXISTS `spmjp`.`leagues` (
	PRIMARY KEY(`id`),
	`id` 	     INT	  NOT NULL AUTO_INCREMENT,
	`country_id` INT	  NOT NULL,
	`name`	     VARCHAR(256) NOT NULL,
	FOREIGN KEY(`country_id`)
	REFERENCES `spmjp`.`countries`(`id`)
);
