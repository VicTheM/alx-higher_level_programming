#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=db,
            charset="utf8"
    )
    cur = conn.cursor()
    stmt = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id;
    """
    cur.execute(stmt)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
