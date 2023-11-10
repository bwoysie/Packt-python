#my solution
while True:
  test = input("say something: ")
  if test == '\end':
      print('its good weather today. how is the weather there'.capitalize())
      break
    
  else:
    continue 
  print('how are you'.capitalize())

  #Ardit's solution

def sentence_maker(phrase):
    interrogatives = ("how","why","what","are","will")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
      return "{}?".format(capitalized)
    else:
      return "{}.".format(capitalized)
            
print(sentence_maker("how are you doing"))



