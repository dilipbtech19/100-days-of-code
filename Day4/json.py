import json

with open('try.json') as json_file:
    data = json.load(json_file)

# print(type(data['value']))

for id in data['value']:
    print(id['id'])
