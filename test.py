#!/usr/bin/env python

import unittest, sys, os
from lsqlite import lsqlite

class lsqliteTestClass(unittest.TestCase):

    def setUp(self):
        projectPath=sys.path[0]
        self.dbFile=os.path.join(projectPath,'test.db')
        self.tdb=lsqlite(self.dbFile)

    def tearDown(self):
        os.unlink(self.dbFile)

    def test_execute(self):
        res = self.tdb.execute("select 1")
        self.assertEquals(res, [(1,)])

    def test_create_table_and_tables(self):
        self.tdb.create_table("t1", {
            "id":"INTEGER PRIMARY KEY",
            "name": "TEXT"})
        res = self.tdb.tables()
        self.assertEquals(res, ['t1'])

    def test_insert_data(self):
        self.test_create_table_and_tables()
        self.tdb.insert_data("t1",{
            "id":1,
            "name":"aaa"})
        res = self.tdb.execute("select * from t1")
        self.assertEquals(res, [(1, u'aaa')])



if __name__ == '__main__':
    unittest.main()



