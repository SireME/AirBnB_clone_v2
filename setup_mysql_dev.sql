

-- Check if database does not exists and create it
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if user exists and create one accodingly
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- grant created user all priviledges on the created database 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';


-- grant select privileges on the performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

--apply changes
FLUSH PRIVILEGES;

-- Set FOREIGN_KEY_CHECKS back to its default value
SET FOREIGN_KEY_CHECKS=1;


