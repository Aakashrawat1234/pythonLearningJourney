import json
with open('states.json') as f:
 data=json.load(f)


for state in data['states']:
    print(state['name'])
    del state['area_code']

with open('states2.json',"w") as f:
    json.dump(data,f,indent=2)
