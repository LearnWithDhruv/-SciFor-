import json

json_data = '''
{
     "name": "Dhruv",
     "age": 20,
     "city": "New Delhi",
     "hobbies": ["Badminton", "Reading"],
}
'''

data = json.loads(json_data)

name = data['name']
age = data['age']
city = data['city']
hobbies = data['hobbies']

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Hobbies:", hobbies)


if name in data:
    print("'name' key exists in JSON data")

else:
    print("'name' key does not exists in JSON data")

data['age'] = 21

data['country'] = "India"

updated_json_data = json.dumps(data, indent=4)

print("\nUpdated Information:")
print(updated_json_data)
