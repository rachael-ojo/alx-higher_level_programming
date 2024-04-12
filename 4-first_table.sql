-- first_table.sql

-- Check if the database name is provided as an argument
SET @db_name = REPLACE('$1', "'", "''");

-- Use the specified database
USE @db_name;

-- Query to retrieve the name of the first table in the specified database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = @db_name
ORDER BY table_name
LIMIT 1;