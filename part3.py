#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

def isPrime(number):
    for i in range(2,number-1):
        if number % i == 0:
            return False
    return True

ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): #for loop appends 5 ranNums to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list


print("Generated list:",ranNums) #print the list!

random_number_to_search = int(input("what number are you searching for?"))
print("Searching for number:", random_number_to_search)

#change message depending on if it was found
if random_number_to_search in ranNums:
    print("Number",random_number_to_search,"found in the list!")
else:
    print("Number",random_number_to_search,"not found in the list.")

# Calculate values
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

# 3 characteristics: 

# Average of integers: 
print("The average of all the numbers is",total_value/len(ranNums))
# Greatest even number:
foundEven = False
for index in range(len(ranNums)-1,-1,-1): # The list is already sorted so just start from the last element to find the largest even number
    if ranNums[index] % 2 == 0:
        print("The largest even number is", ranNums[index])
        foundEven = True
        break

if not foundEven:
    print("There are no evens in the list")

# Smallest prime number

foundPrime = False
for number in ranNums:
    if isPrime(number):
        print("The smallest prime number is",number)
        foundPrime = True
        break

if not foundPrime:
    print("There are no primes in the list")
while True:
    if len(ranNums) == 0:
        print("number not found")
        break
    middle_index = len(ranNums)//2
    middle_value = ranNums[middle_index]
    if middle_value > random_number_to_search:
        ranNums = ranNums[:middle_index]
    elif middle_value < random_number_to_search:
        ranNums = ranNums[middle_index-1:]
    else: 
        print(middle_value)
        break
