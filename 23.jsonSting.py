import json
people_string= '''
{
    "people":[
        {
            "name":"Jhon_Smith",
            "phone":"54786889",
            "email":"jhon@gmail.com",
            "has_licence":false
        },
        {
            "name":"Aakash",
            "phone":"54477876889",
            "email":null,
            "has_licence":true
        }
    ]
}
'''

data=json.loads(people_string)
print(data)


for person in data['people']:
    print(person['name'])
    del person['phone']


new_string=json.dumps(data,indent=2,sort_keys=True)

print(new_string)