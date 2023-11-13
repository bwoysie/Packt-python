#These are similar to for loops..
#the differnce is the list comprehension is written on one line 
#they are used when you want to construct a list..so its a loop 
#that constructs a list


#using a for loop 
temps = [221,234,345,674]
new_temps = []
# to divide all the numbers in the list by 10 ..we use a loop
for temp in temps:
  #first crate a place to store the results..see line 7
  new_temps.append(temp / 10)

print(new_temps)

# *************** a list compherension

new_temps = [temp / 10 for temp in temps]
# for the variable in the list do whatever is on the left
new_temps = [temp * 10 for temp in temps]
print(new_temps)