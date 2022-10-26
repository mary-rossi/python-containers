### Exercise 1
students = ["Mary", "Ryan", "Chris", "Michelle"]

print(students[1]) # second
print(students[-1]) # last


### Exercise 2
foods = ("apple", "orange", "banana", "chicken")

for food in foods:
   print(food + " is a good food")


### Exercise 3
for food in foods[-2:]:
   print(food)


### Exercise 4
home_town = {
   "city": "The Colony",
   "state": "Texas",
   "population": 48000
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')


### Exercise 5
for key, value in home_town.items():
   print(f'{key} = {value}')


