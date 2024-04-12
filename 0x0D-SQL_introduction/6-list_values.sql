-- list_values.sql

-- Check if the database name, table name, and column name are provided as arguments
SET @db_name = REPLACE('$1', "'", "''");
SET @table_name = REPLACE('$2', "'", "''");
SET @column_name = REPLACE('$3', "'", "''");

-- Use the specified database
USE @db_name;

-- Query to retrieve distinct values from the specified column
SET @sql_query = CONCAT('SELECT DISTINCT ', @column_name, ' FROM ', @table_name, ';');

-- Execute the SQL query
PREPARE stmt FROM @sql_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;