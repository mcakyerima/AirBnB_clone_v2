-- Prepares a MySQL server for the project
-- Grants usage on all databases to 'hbnb_dev' user at localhost
-- Creates the hbnb_dev_db database if it does not exist
-- Creates the hbnb_dev user if it does not exist, identified by 'hbnb_dev_pwd'
-- Switches to the hbnb_dev_db database
-- Grants all privileges on hbnb_dev_db to 'hbnb_dev' user at localhost
-- Switches to the performance_schema database
-- Grants select privileges on performance_schema to 'hbnb_dev' user at localhost
-- Flushes privileges to apply changes

GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
