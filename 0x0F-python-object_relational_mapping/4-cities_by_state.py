#!/usr/bin/python3
"""The function constructs an SQL query string to select all columns (*) from the cities table in the specified database."""

import MySQLdb
import sys

def list_cities(username, password, database):
    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=username, passwd=password, db=database)

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Define the SQL query to select all cities sorted by id
        query = "SELECT * FROM cities ORDER BY id ASC;"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the result set
        results = cursor.fetchall()

        # Display the results in the specified format
        for row in results:
            print(row)  # Output each row as a tuple

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <host> <@Adeola1234567> <hbtn_0e_0_usa>")
        sys.exit(1)

    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the list_cities function with provided arguments
    list_cities(username, password, database)
