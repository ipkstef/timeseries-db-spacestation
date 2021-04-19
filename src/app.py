from data import create_user
import os
import requests 
import json
from datetime import datetime



database = os.path.relpath('./data/iss_timeseries.db')

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
obj = json.loads(response.content)

def main():
	create_user.write_user(obj['timestamp'],obj['iss_position']['latitude'], obj['iss_position']['latitude'],datetime.now().date())





if __name__ == '__main__':
	main()