-- create_database_if_missing.sql

-- Specify the database name you want to create if it doesn't exist
SET @database_name = 'your_database_name';

-- Check if the database exists
SELECT IF(
    EXISTS (
        SELECT 1
        FROM information_schema.schemata
        WHERE schema_name = @database_name
    ),
    'Database already exists',
    'Database does not exist, creating...'
) AS message \G

-- Create the database if it doesn't exist
IF NOT EXISTS (
    SELECT 1
    FROM information_schema.schemata
    WHERE schema_name = @database_name
)
THEN
    CREATE DATABASE IF NOT EXISTS `your_database_name`;
    SELECT 'Database created successfully' AS message \G
END IF;