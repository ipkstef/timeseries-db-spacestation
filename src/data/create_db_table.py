import sys 
import os 
sys.path.append(os.path.abspath("../"))
from comconnection import startdb_connection
import sqlite3
from sqlite3 import Error




""" create table function accepts the connection object from create_connection and an sql statement"""
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



	""" create a table from the create_table_sql statement 'sql_create_$projectid_table'

	define your variables fool

	:param conn: Connection Object
	:param create_table_sql: a CREATE TABLE statement
	:return 

	"""


def initialize_table():
    database = "iss_timeseries.db"

    sql_create_iss_table = """ CREATE TABLE IF NOT EXISTS iss_time_series (
                                        unixtimestamp integer PRIMARY KEY,
                                        latitude real NOT NULL,
                                        longitude real 	NOT NULL,
                                        est_date text
                                    )"""



    # create a database connection
    conn = startdb_connection.create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_iss_table)

    else:
        print("error line 51")


if __name__ == '__main__':
    initialize_table()






