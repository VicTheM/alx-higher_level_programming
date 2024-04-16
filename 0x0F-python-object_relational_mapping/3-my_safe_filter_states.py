#!/usr/bin/python3
"""This script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=db,
            charset="utf8",
    )
    cur = conn.cursor()
    stmt = "SELECT * FROM states WHERE name = %(state_name)s  ORDER BY id ASC"
    cur.execute(stmt, {"state_name": state_name})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
