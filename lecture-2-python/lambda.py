#we want to sort this list
people = [
    {"name": "Harry", "house": "house1"},
    {"name": "CHo", "house": "jouse1"},
    {"name": "Pepe", "house": "house2"}
]

#def f(person):
#    return person["name"]
#
#people.sort(key=f)
#The above expression is the same as the following:
people.sort(key = lambda person: person["name"])

print(people)