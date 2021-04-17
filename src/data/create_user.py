from create_db_table import create_connection
import random


def create_user(conn, users):
	"""

	Create a new user

	:param conn:
	:param user:
	:return:
	"""

	sql = ''' INSERT INTO users (id, name, phonenum) VALUES (?,?,?) '''

	cur = conn.cursor()
	cur.execute(sql,users)
	conn.commit

	return cur.lastrowid


def write_user():

	database = "employee.db"

	conn = create_connection(database)
	with conn:

		user_1 = (7035558009,'Jane Doe',random.randint(100,999))

		create_user(conn, user_1)

if __name__ == '__main__':
	write_user()
