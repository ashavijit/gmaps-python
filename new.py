  
import json
from time import *
import requests


serviceurl = "https://maps.googleapis.com/maps/api/distancematrix/json?"

while True:
	start = ("|".join(input("Enter origins: ").split(",")))
	end  = ("|".join(input("Enter destinations: ").split(",")))
	key = " " # Your API Key
	
	extend = {'units':'metric','origins':start,'destinations':end, 'key':key, 'departure_time':'now', 'mode':'driving', 'traffic_model':'best_guess'}
	
	try:
	
		r = requests.get(serviceurl, params = extend )
	
	except requests.ConnectionError as e:
		
		print()
		print("There is no Internet connection!")
		print("Error",e)
		break
	
	js = r.json()
	if js['rows'][0]['elements'][0]['status'] == "OK":
		o = 0
		for i in js['rows']:
			print()
			print(js['origin_addresses'][o])
			d = 0
			o += 1
			print()
			for j in i['elements']:
				print(js['destination_addresses'][d])
				print("Distance:",j['distance']['text'])
				print("Average Duration:",j['duration']['text'])
				print("Live Traffic:",j['duration_in_traffic']['text'])
				d += 1
				print()
		
	else:
		print("Invalid Location")
		print()