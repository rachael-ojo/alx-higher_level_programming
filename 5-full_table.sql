-- full_table.sql

-- Check if the database name and table name are provided as arguments
SET @db_name = REPLACE('$1', "'", "''");
SET @table_name = REPLACE('$2', "'", "''");

-- Use the specified database
USE @db_name;

-- Query to retrieve all data from the specified table
SET @sql_query = CONCAT('SELECT * FROM ', @table_name, ';');

-- Execute the SQL query
PREPARE stmt FROM @sql_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;