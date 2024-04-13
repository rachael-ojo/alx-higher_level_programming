-- Cretae_table 'second_table' in database 'hbtn_0c_0'
-- Add_props (id INT), (name VAR-CHAR(256)), (Score INT)
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), Score INT);
-- Script should create maximum of 4 records
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES (1, "John", 10);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES (2, "Alex", 3);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES (3, "Bob", 14);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES (4, "George", 8);