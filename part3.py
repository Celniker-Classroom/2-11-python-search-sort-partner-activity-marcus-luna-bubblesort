#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): #for loop appends 5 ranNums to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list


print("Generated list:",ranNums) #print the list!

random_number_to_search = int(input("what number are you searching for?"))
print("Searching for number:", random_number_to_search)

if random_number_to_search in ranNums:
    print("Number",random_number_to_search,"found in the list!")
else:
    print("Number",random_number_to_search,"not found in the list.")

minimum_value = min(ranNums)

print("the minimum value is", minimum_value)

maximum_value = max(ranNums)

print("the maximum value is", maximum_value)

total_value = 0
for num in ranNums:
    total_value+=num
print("the total value is", total_value)

ranNums.sort()
print("your sorted list is", ranNums)