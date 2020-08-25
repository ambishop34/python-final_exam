"""
Name: UKHUREBOR OSAGIE NATHANIEL
StudentID:  MSE0103

---------------------------
Question 3:

Write a program in the python programming language using data from the datafile.txt
as Command Line Arguments. The result is saved to the database file dbFPT.sqlite.
Create the table with information:
CREATE TABLE InFos (ProCode INTEGER, Deleted TEXT)
The program prints the number of processed records,
the first 3 rows of the table when sorted in descending order by ProjectCode.

"""

# import sqlite
import sqlite3 as lite

# connect data to sqlite db created as q3
connection = lite.connect('q3.db')

def connect_db_and_create_table(connection=connection):
    """
    connect_db_and_create_table connects to the db and creates the table InFos

    Then writes to the db
    """    ""

    with connection:

        cur = connection.cursor()

        cur.execute("DROP TABLE IF EXISTS InFos")
        cur.execute("CREATE TABLE InFos(ProCode INT, Deleted TEXT)")
        cur.execute("INSERT INTO InFos VALUES(1,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(2,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(9,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(10,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(11,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(12,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(13,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(14,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(15,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(16,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(3,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(4,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(5,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(6,'Undelete')")
        cur.execute("INSERT INTO InFos VALUES(7,'Delete')")
        cur.execute("INSERT INTO InFos VALUES(8,'Undelete')")


def retrieve_data_from_sqlite(connection=connection):
    """
    retrieve_data_from_sqlite retrieves the data from the sqlite db

    Parameters
    ----------
    connection : string, optional
        string connection, by default connection
    """    ""

    with connection:

        cur = connection.cursor()

        cur.execute("""SELECT * FROM InFos
                    ORDER BY ProCode DESC
                    LIMIT 3""")

        data = cur.fetchall()

        for item in data:
            print(item)


def write_sqlite_file(data):
    """
    write_sqlite_file writes the data to an sqlite file

    Parameters
    ----------
    data : string
        data to write
    """    ""
    sqlite_file = open('dbFPT.sqlite', 'w')

    with sqlite_file:
        sqlite_file.write(data)

# connect to sqlite db and create tables
create_db_and_tables = connect_db_and_create_table()

# retrieve data from sqlite tables
retrieve_data_from_sqlite()

# write the file
with connection:
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS InFos")
    cur.execute("CREATE TABLE InFos(ProCode INT, Deleted TEXT)")
    cur.execute("INSERT INTO InFos VALUES(1,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(2,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(9,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(10,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(11,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(12,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(13,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(14,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(15,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(16,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(3,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(4,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(5,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(6,'Undelete')")
    cur.execute("INSERT INTO InFos VALUES(7,'Delete')")
    cur.execute("INSERT INTO InFos VALUES(8,'Undelete')")

    data = '\n'.join(connection.iterdump())

    # write the sqlite file
    write_sqlite_file(data)
