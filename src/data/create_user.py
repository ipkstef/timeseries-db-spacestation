import sys 
import os 
sys.path.append(os.path.abspath("../"))
from comconnection import startdb_connection


def create_user(conn, users):
	"""

	Create a new user
b
	:param conn:
	:param user:
	:return:
	"""

	sql = ''' INSERT INTO iss_time_series (unixtimestamp, latitude, longitude, est_date) VALUES (?,?,?,?) '''

	cur = conn.cursor()
	cur.execute(sql,users)
	conn.commit

	return cur.lastrowid


def write_user(unixtimestamp,latitude,longitude,est_date):

	database = os.path.relpath('./data/iss_timeseries.db')

	conn = startdb_connection.create_connection(database)
	with conn:

		entry_1 = (unixtimestamp, latitude, longitude,est_date)

		create_user(conn, entry_1)

if __name__ == '__main__':
	write_user()

