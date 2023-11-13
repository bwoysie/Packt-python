# first analyse and split task into smaller parts
#make a function
#recognise your data types so you know what functions to use
#the first part of the task is to capitalize a sentence(phrase)
# open a terminal using python and try it out
#decide so you need a conditional..??? are decisions to be made
#always think about using variables to make your code more readable seee lines 11 and 13

def sentence_maker(phrase):
  # to capitallize a string(phrase)
  interrogatives = ("how","what","why","are")
  capitalized = phrase.capitalize()
  #if phrase.startswith(("how","what","why","are")):
  if phrase.startswith(interrogatives):
    return '{}?'.format(capitalized)
  else:
    return "{}.".format(capitalized)
  
#print(sentence_maker("whats going on ..how you doing"))**this line was just to test the function
#below I used a while loop to keep asking a question to get user input and used a word to break the loop

# I made a empty list to capture and store user input

results = []
while True:
  user_input = input('Say something: ')
  if user_input == '\end':
    break
  else:
    results.append(sentence_maker(user_input))

# print(results) to test how to use it with the first function 

print(results)

#now to make all the user input to make one sentence use the join function 

print(" ".join(results))