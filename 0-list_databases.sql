-- list_databases.sql

-- Select all database names from the information_schema
SELECT schema_name AS DatabaseName
FROM information_schema.schemata
ORDER BY schema_name;