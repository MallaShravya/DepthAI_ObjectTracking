import sqlite3
import pandas as pd

# Create a SQL connection to our SQLite database
con = sqlite3.connect("trackletData.db")

cur = con.cursor()

# Return all results of query
cur.execute('SELECT * FROM ids')
# df = pd.read_sql_query("with a as (SELECT id, min(starttime) as start from ids group by id),
#                             b as (SELECT id, max(endtime) as end, status from ids group by id)
#                         select a.id, a.start, b.id, b.end, b.status from a join b on a.id = b.id group by id", con)

# df = pd.read_sql_query("select id from ids", con)

df = pd.read_sql_query("with a as (select id, min(starttime) as start from ids group by id), b as (select id,"
                       "max(endtime) as end, status from ids group by id)"
                       "select a.id, a.start, b.end, b.status from a join b on a.id = b.id", con
                       )
print(df)

# cur.fetchall()

# Return first result of query
# cur.execute('SELECT species FROM species WHERE taxa="Bird"')
# cur.fetchone()

# Be sure to close the connection
con.close()