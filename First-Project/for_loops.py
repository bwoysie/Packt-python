#for loops

monday_temperatures = [9.1,8.3,7.2,10.9, 6.4]
# print(monday_temperatures[1])
# print(round(monday_temperatures[0]))
# print(round(monday_temperatures[1]))
# print(round(monday_temperatures[2]))


#do this instead
#choose a variable eg. temperature use the key words for and in 

for temperature in monday_temperatures:
  print(round(temperature))
  print('done')

for letter in 'hello':
  print(letter.title())

# looping over a dictionary
# the options are items, keys or values
# so chose a variable eg grades and then use the options of the dictionary

student_grades = {'Mary': 95.3, "Tom": 87.2, 'Harry': 99.9,"Billy": 79.9}
for grades in student_grades.items():
  print(grades)

for grades in student_grades.keys():
  print(grades)  

for grades in student_grades.values():
  print(grades)  

# while loops
# run as long as condition is true

user_name = ''

# while user_name != "pypy":
#   user_name = input("Enter your name : ")

# A better way to do this is below

while True:
  username = input("ENter username: ")
  if username == 'pypy':
      break
  else:
    continue  





