#!/usr/bin/python3
"""taske select"""

import mysql.connector
import sys

def select_states(username, password, db_name):
    try:
        db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            database=db_name
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except mysql.connector.Error as e:
        print("MySQL Error {}: {}".format(e.errno, e.msg))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    select_states(sys.argv[1], sys.argv[2], sys.argv[3])
