import json
import requests
from itertools import groupby
import datetime


url = 'https://enerity-api.azureedge.net/outagemap/tailored/summary/'


r = requests.get(url)

fmt = "%Y-%m-%d %H:%M:%S"
time_epoch = r.json()['timestamp']
print(time_epoch)
timestamp = datetime.datetime.fromtimestamp(float(time_epoch)/1000.)
print(timestamp.strftime(fmt)) # prints 2012-08-28 02:45:17

input_dict = r.json()['areas']
 
print(type(input_dict))

print(json.dumps(r.json()['timestamp']))
print(json.dumps(r.json()['areas'], ensure_ascii=False, indent=5))
print("\n")
print(json.dumps(r.json()['areas'][0]['name'], ensure_ascii=False, indent=1))

data = json.dumps(r.json()['areas'], ensure_ascii=False, indent=1)

for each in input_dict:
	print(f"{timestamp.strftime(fmt)};{each['name']};{each['total']}")


# for each in data:
# 	if i=='alias'  each[i]:
# 		del each[i]
# 	if 'planned' in each:
# 		del each['planned']
#	print(each)
# data.sort(key=lambda data: data['name'])
# groups = groupby(data, lambda data: data['name'])

# if 'alias' in data:
#     del data['alias']

# print(type(data))

# for name, group in groups:
#     print(name)
#     for data in group:
#         print('\t', data)


