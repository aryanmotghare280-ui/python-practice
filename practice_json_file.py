
import json

data = {'name': "Rahul",



'salary': 35000,



'department': "IT"}

result=json.dumps(data)

print(result)
print(type(result))




import json

data = '{"city": "Nagpur", "temperature": 32}'

result = json.loads(data)
print(result['city'])
print(result['temperature'])
print(type(result))





# Ab hum JSON data ko ek file mein save karna seekhenge.
# Task: Neeche diye data ko student.json file mein save karo.


import json

data = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(data, file)

print("File created successfully!")


#abhi isse file ko read krna hai toh load ka use honga
import json

with open("student.json", "r") as file:
    result = json.load(file)

print(result)
print(result["name"])
print(type(result))


