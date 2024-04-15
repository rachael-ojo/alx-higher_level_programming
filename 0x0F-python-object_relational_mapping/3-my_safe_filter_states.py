#!/usr/bin/python3
"""Function that is typically used to access, modify, or delete data from a database."""

import MySQLdb
import sys

def filter_states(username, password, database, state_name):
    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=username, passwd=password, db=database)

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Define the SQL query with parameterized input
        query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;"

        # Execute the query with the state_name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all matching rows
        results = cursor.fetchall()

        # Display the results in the specified format
        if results:
            for row in results:
                print(row)  # Output the (id, name) tuple
        else:
            print("No matching states found in the database.")

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python script.py <host> <@Adeola1234567> <hbtn_0e_0_usa> <Arizona>")
        sys.exit(1)

    # Parse command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the filter_states function with provided arguments
    filter_states(username, password, database, state_name)
