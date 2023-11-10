def mean(mylist):
    the_mean = sum(mylist) /len(mylist)
    # return the_mean  with out a return statement python returns None in the terminal
    return the_mean
print(mean([1,2,3,4,5]))  

#  Functions and conditionals to calculate the mean of a dictionary

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /len(value)

    else:    
        the_mean = sum(value) /len(value)
    # return the_mean  with out a return statement python returns None in the terminal

    return the_mean
student_grades = {'mary': 9.1,'Sam': 8.8, 'John': 7.5}
print(mean(student_grades))  


def weather_condition (temperature):
    if temperature > 8:
        return "warm"
    else:
        return "cold"

# print('The weather outside is ' + weather_condition(5))
# to get a input from the user we use the input function

user_input = float(input("please enter the temperature : "))
print('The weather outside is ' + weather_condition(user_input))


#user input with string formatting using %s

user_input = input("Enter your name: ")
message = "Hello %s!" % user_input
# %s is the same as {}
#using the f string
message = f"Hello {user_input} how are you "
print (message)
#message gets  over written
# print (message)