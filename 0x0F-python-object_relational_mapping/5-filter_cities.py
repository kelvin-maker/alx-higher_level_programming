#!/usr/bin/python3
"""
List all states matching given name from a MySQL db on localhost at port 3306
"""

import sys
import MySQLdb

if __name__ == '__main__':
        db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                             db=sys.argv[3], port=3306)

        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = '{}';".format(sys.argv[4]))
        
        states = cur.fetchall()

        print(", ".join([state[1] for state in states]))
