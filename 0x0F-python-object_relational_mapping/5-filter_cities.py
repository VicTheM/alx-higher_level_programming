#!/usr/bin/python3
"""This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

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
            charset="utf8"
    )
    cur = conn.cursor()
    stmt = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY '{}'
    ORDER BY cities.id;
    """.format(state_name)
    cur.execute(stmt)
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        if i + 1 < len(query_rows):
            print(query_rows[i][0], end=", ")
        else:
            print(query_rows[i][0], end="")
    print()
    cur.close()
    conn.close()
