# This program computes the sum, difference,
# product, average, distance (absolute value of difference,)
# & the min/max values between two given integers.

numOne = int(0)
numTwo = int(0)

sum = int(0)
difference = int(0)
product = int(0)
average = int(0)
absValue = int(0)
maxNum = int(0)
minNum = int(0)

# print to user what the program does
print("This program performs various calculations for two given integers. ")
print(" ")

# prompt user to input first integer
numOne = (input("Please enter a whole number greater than zero: "))
numOne = int(numOne)

# catch invalid inputs for nums other than integers    
if numOne <= 0:
     print(" ")
     print("Error: must enter an integer. ")
     print(" ")
     numOne = (input("Please enter a whole number greater than zero: "))
     numOne = int(numOne)
# else if valid input, print integer and proceed to second input prompt
else: numOne >= 0
numOne = int(numOne)
print("You entered: ",(numOne))
print (" ")

# prompt user to input second integer
numTwo = (input("Please enter a whole number greater than zero: "))
numTwo = int(numTwo)

# catch invalid inputs for nums other than integers
if numTwo < 0:
     print(" ")
     print("Error: must enter an integer. ")
     print(" ")
     numTwo = (input("Please enter a whole number greater than zero: "))
     numTwo = int(numOne)
# else if valid input, print integer and proceed to calculations
else: numTwo > 0
numTwo = int(numTwo)
print("You entered: ",(numTwo))
print (" ")

print("...")
print(" ")

# perform each calculation and print results to user on separate lines
sum = numOne + numTwo
print("The sum of the numbers is: ", sum)
print(" ")

difference = numOne - numTwo
absValue = abs(difference)
print("The difference between the numbers is: ", difference)
print(" ")

product = numOne * numTwo
print("The product of the numbers is: ", product)
print(" ")

average = (numOne + numTwo)/2
average = int(average)
print("The average of the numbers is: ", average)
print(" ")

print("The distance (absolute value) between the numbers is: ", absValue)
print(" ")

maxNum = max(numOne, numTwo)
print("The larger of the numbers is: ", maxNum)
print(" ")

minNum = min(numOne, numTwo)
print("The smaller of the numbers is: ", minNum)
print(" ")

