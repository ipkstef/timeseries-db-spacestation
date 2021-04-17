import sqlite3
from sqlite3 import Error


def create_connection(db_file):
	""" lets make a function that returns a connection object"""

	conn = None 

	try:

		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		return conn


	except Error as e:

		print(e)

	return conn


""" create table function accepts the connection object from create_connection and an sql statement"""
def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement 'sql_create_$projectid_table'

	define your variables fool

	:param conn: Connection Object
	:param create_table_sql: a CREATE TABLE statement
	:return 

	"""
 	try:
 		c = conn.cursor()
 		c.execute(create_table_sql)
 	except Error as e:
 		print(e)



def main():
    database = "employee.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    )"""



    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)

    else:
        print("error line 63")


if __name__ == '__main__':
    main()






