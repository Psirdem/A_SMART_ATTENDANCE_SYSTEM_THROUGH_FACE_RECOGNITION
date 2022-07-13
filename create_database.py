import sqlite3

conn = sqlite3.connect('Database.db')

c = conn.cursor()

sql = """
DROP TABLE IF EXISTS StudentDetails;
CREATE TABLE StudentDetails(
           name text,index_no integer PRIMARY KEY, programme text
);
"""
c.executescript(sql)

conn.commit()











































conn.close()