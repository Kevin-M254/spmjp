CREATE DATABASE IF NOT EXISTS spmjp_dev_db;
CREATE USER IF NOT EXISTS 'spmjp_dev' @'localhost' IDENTIFIED BY 'spmjp_dev_pwd';
GRANT ALL PRIVILEGES ON spmjp_dev_db.* TO 'spmjp_dev' @'localhost';
GRANT SELECT ON perfomance_schema.* TO 'spmjp_dev' @'localhost';
