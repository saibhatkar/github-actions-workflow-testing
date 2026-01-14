# This code prompts the user to enter two numbers, calculates their sum, and then displays the result.

enterTwoNumbers = input("Please enter two numbers separated by a space: ")
num1, num2 = map(int, enterTwoNumbers.split())
sumResult = num1 + num2
print("The sum of", num1, "and", num2, "is:", sumResult)

