#!/usr/bin/python3
"""the  task"""
import MySQLdb
import sys


def select_states(username, password, my_db):

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="root",
                           db=my_db,
                           charset="utf8")
    cur = conn.cursor()
    sql_query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(sql_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    select_states(sys.argv[1], sys.argv[2], sys.argv[3])
