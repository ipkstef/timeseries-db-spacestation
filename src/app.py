from data import create_user
import os
import requests 
import json
from datetime import datetime
import time
import logging



database = os.path.relpath('./data/iss_timeseries.db')

url = "http://api.open-notify.org/iss-now.json"
logging.basicConfig(format='%(levelname)s:%(asctime)s: %(message)s', filename='myapp.log', level=logging.INFO)

def main():
	while True:
		try:
			response = requests.get(url)
			obj = json.loads(response.content)
		except requests.ConnectionError as e:
			print(e, + "this is in response requests error")
			logging.error('Connection Error to the api')
		else:
			#write to db
			create_user.write_user(obj['timestamp'],obj['iss_position']['latitude'], obj['iss_position']['longitude'],datetime.now().date())
			
		time.sleep(5)






if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		logging.critical('This is a hard crash, db missing or someshit ')
