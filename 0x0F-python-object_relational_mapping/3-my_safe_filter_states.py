#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                    db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * \
        FROM states \
        WHERE name = '{}';".format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)
                                                            
