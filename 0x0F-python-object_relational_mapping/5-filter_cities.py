#!/usr/bin/python3
"""Function connects to a MySQL database, executes an SQL query to retrieve and display all cities from a specified table (cities) in the database."""

import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=username, passwd=password, db=database)

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Define the SQL query with parameterized input to select cities by state name
        query = "SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"

        # Execute the query with state_name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        results = cursor.fetchall()

        # Display the results in the specified format
        for row in results:
            print(row)  # Output each (id, name) tuple for cities in the specified state

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <root> <@Adeola1234567> <hbtn_0e_0_usa> <Texas>")
        sys.exit(1)

    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the list_cities_by_state function with provided arguments
    list_cities_by_state(username, password, database, state_name)
