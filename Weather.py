import urllib.request
import json

city = input('Pick city: ')

APIKEY = '4800a363c37fb3ab0b51b2a61f088d94'

link = 'http://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID='+APIKEY+'&units=metric'

with urllib.request.urlopen(link) as f:
	data = json.load(f)
	
#print(data.keys()) # -> ['cod', 'message', 'cnt', 'list', 'city']
#print(data['list'])

for i in range(len(data['list'])):
	if '15:00' in data['list'][i]['dt_txt']:
		print('\nDate:',data['list'][i]['dt_txt'])
		print('Max temperature:', data['list'][i]['main']['temp_max'])
		print('Min temperature:', data['list'][i]['main']['temp_min'])