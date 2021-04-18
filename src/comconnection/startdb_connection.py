import sqlite3
from sqlite3 import Error



def create_connection(db_file):
	""" lets make a function that returns a connection object"""

	conn = None 

	try:

		conn = sqlite3.connect(db_file)
		#print("Connection to db Established")
		return conn


	except Error as e:

		print(e)

	return conn


if __name__ == '__main__':
	create_connection()