#!/usr/bin/python3
"""Function retrieves and prints the first 5 states from the states table in a specified MySQL database"""

import sys
import MySQLdb

def list_states(username, password, database):
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Prepare SQL query to select the first 5 states ordered by id
        sql = "SELECT * FROM states ORDER BY id ASC LIMIT 5"

        cursor.execute(sql)
        states = cursor.fetchall()

        for state in states:
            print(f"({state[0]}, '{state[1]}')")

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <host> <@Adeola1234567> <hbtn_0e_0_usa>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
