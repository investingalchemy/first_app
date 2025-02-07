#practicing dictionaries
dict_a = {"name":"milk", "cost": 6.5, "store": "Save-On", "amount": 2}
print(dict_a.items())

#practice excercise
#create and accessing values
book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
print(book["author"])

#Adding and updating entries:
profile = {}
profile['name'] = 'Alice'
profile['age'] = 30
profile['city'] = 'Paris'
print(profile)
profile['city'] = 'London'
print(profile)

#removing and retrieving keys and values
student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
student.pop('subject')
print(student)


