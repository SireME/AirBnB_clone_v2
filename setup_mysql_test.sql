
-- Check if database does not exists and create it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if user exists and create one accodingly
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant created user all priviledges on the created database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privileges on the performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush to apply changes
FLUSH PRIVILEGES;

-- Set FOREIGN_KEY_CHECKS back to its default value
SET FOREIGN_KEY_CHECKS = 1;
