#!/usr/bin/python3
"""the first task"""
import MySQLdb
import sys


def select_states(username, password, my_db, searched):

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="root",
                           db=my_db,
                           charset="utf8")
    cur = conn.cursor()
    sql_query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(searched)
    cur.execute(sql_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    select_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
