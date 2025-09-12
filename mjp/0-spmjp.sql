-- Creates database spmjp with table countries
CREATE DATABASE IF NOT EXISTS `spmjp`;
CREATE TABLE IF NOT EXISTS `spmjp`.`countries` (
	PRIMARY KEY(`id`),
	`id`	INT		NOT NULL AUTO_INCREMENT,
	`name`  VARCHAR (256)   NOT NULL
);
