from data import create_user
import os
import urllib.request as urllib2
import json
from datetime import datetime


database = os.path.relpath('./data/iss_timeseries.db')

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj = json.loads(response.read())

def main():
		create_user.write_user(obj['timestamp'],obj['iss_position']['latitude'], obj['iss_position']['latitude'],datetime.now().date())





if __name__ == '__main__':
	main()