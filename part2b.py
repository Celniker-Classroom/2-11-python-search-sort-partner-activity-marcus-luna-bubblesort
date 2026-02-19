#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): #for loop appends 5 ranNums to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list


print(ranNums) #print the list!

random_number_to_search = randint(1, 20)

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for number in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if number == random_number_to_search:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found