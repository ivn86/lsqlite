lsqlite
-------
Lightweight and simple API for work with SQLite database in Python.

What it is
----------

I have written this library for easy access to SQLite databases, when writing scetches in QPython. It is not ORM, just simple way to make life easier.

It can:

* create, truncate, drop tables
* show list of exists tables
* show table detail info
* insert data
* execute any query

Example of use
--------------

    import os, sys
    from lsqlite import lsqlite

    if __name__ == '__main__':

        projectPath=sys.path[0]
        dbFile=os.path.join(projectPath,'lsqlite.db')
        db = lsqlite(dbFile)

Example table creating

        db.create_table(
                "artist",
                {
                    "artistid": "INTEGER PRIMARY KEY",
                    "artistname": "TEXT"
                }
                )
        db.create_table(
                "track",
                {
                    "trackid": "INTEGER",
                    "trackname": "TEXT",
                    "trackartist": "INTEGER"
                },
                ("FOREIGN KEY(trackartist) REFERENCES artist(artistid)"))

Print out tables names
        
        print "Tables: %s" % db.tables()
        # Tables: [u'artist', u'track']

Print out columns for table 'artist'
    
        print "Table 'artist' collumns: ", db.columns('artist')
        # Table 'artist' collumns:  ['artistid', 'artistname']

Print out columns for table

        print "Info for table 'artist': %s" % db.table_info('artist')
        # Info for table 'artist': [(0, u'artistid', u'INTEGER', 0, None, 1), (1, u'artistname', u'TEXT', 0, None, 0)]

Example data insertion

        db.insert_data("artist", {"artistid":1, "artistname":"Dean Martin"})
        db.insert_data("artist", {"artistid":2, "artistname":"Frank Sinatra"})
        db.insert_data("track", {"trackid":11, "trackname":"That's Amore", "trackartist":1})
        db.insert_data("track", {"trackid":12, "trackname":"Christmas Blues", "trackartist":1})
        db.insert_data("track", {"trackid":13, "trackname":"My Way", "trackartist":2})

Example SQL execution

        print "Frank's songs: %s" % db.execute("SELECT trackname \
                FROM track \
                JOIN artist ON track.trackartist = artist.artistid \
                WHERE \
                artistname LIKE '%Sinatra'")
        # Frank's songs: [(u'My Way',)]

Example truncate data

        db.truncate("track")
        print "Tracks count after truncate: %s" % db.execute("SELECT COUNT(*) FROM track")
        # Tracks count after truncate: [(0,)]

Drop tables

        db.drop_table('track')
        db.drop_table('artist')
