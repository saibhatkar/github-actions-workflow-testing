# This code prompts the user to enter two numbers, calculates their difference, and then displays the result.

enterTwoNumbers = input("Please enter two numbers separated by a space: ")
num1, num2 = map(int, enterTwoNumbers.split())
differenceResult = num1 - num2
print("The difference of", num1, "and", num2, "is:", differenceResult)