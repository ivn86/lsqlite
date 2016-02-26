#!/usr/bin//env python

import sys, os
import sqlite3 as lite

class lsqlite:
    def __init__(self, dbFile):
        self.con = lite.connect(dbFile)

    def tables(self):
        """Show database tables"""
        with self.con:
            __cur=self.con.cursor()
            __cur.execute("SELECT name \
                FROM sqlite_master \
                WHERE type='table';")
            return [f[0] for f in __cur.fetchall()]

    def create_table(self, table, cols, keys=None):
        """Create new table with name {{ table }} and columns like { k:v }.
        keys list for special keys, for example foreign key"""
        __query = "CREATE TABLE '%s' (" % table
        for k,v in cols.iteritems():
            __query += "%s %s," % (k, v)
        if keys <> None:
            for key in keys:
                __query += key
            __query += ","
        __query = __query[:-1]
        __query += ")"
        self.execute(__query)

    def drop_table(self, name):
        """Just drop table"""
        try:
            self.execute("DROP TABLE '%s'" % name)
        except:
            print "Table not found"

    def insert_data(self, table, data):
        """Insert data to table {{ table }} with specify data in dictionary {k:v }"""
        try:
            self.execute("INSERT INTO '%s' %s VALUES %s" % 
                    (table, 
                    tuple(data.keys()), tuple(data.values())
                    )
            )
        except:
            print "Error insert data"

    # TODO: Depricated
    def columns(self, table):
        """Show columns names for table"""
        with self.con:
            __cur=self.con.cursor()
            __cur.execute("SELECT * FROM '%s';" % (table))
            return [f[0] for f in __cur.description]

    def table_info(self, table):
        """Get table info for {{ table }}"""
        try:
            __cur=self.con.cursor()
            __cur.execute("PRAGMA table_info(%s);" % table)
            return __cur.fetchall()
        except:
            print "Error getting table info"

    def execute(self, query):
        """Execute SQL queries"""
        __cur=self.con.cursor()
        try:
            __cur.execute(query)
            return __cur.fetchall()
        except:
            print "Error SQL query execution"
            raise

    def truncate(self, table):
        """Truncate table {{ table }}"""
        self.execute("DELETE FROM '%s';" % (table))

if __name__ == "__main__":
    pass
