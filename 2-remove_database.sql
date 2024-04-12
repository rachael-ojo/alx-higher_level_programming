-- remove_database.sql

-- Define a delimiter to allow semicolons within the stored procedure
DELIMITER $$

-- Create a stored procedure to safely drop the database
CREATE PROCEDURE remove_hbtn_0c_0_database()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42000'
        BEGIN
            -- Error code 1008 (ER_DB_DROP_EXISTS) indicates database doesn't exist
            -- We catch this error and ignore it
        END;

    -- Attempt to drop the database
    DROP DATABASE IF EXISTS hbtn_0c_0;
END $$

-- Reset the delimiter to semicolon
DELIMITER ;

-- Call the stored procedure to remove the database
CALL remove_hbtn_0c_0_database();