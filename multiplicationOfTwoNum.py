# multiplication of two numbers
enterTwoNumbers = input("Please enter two numbers separated by a space: ")
num1, num2 = map(int, enterTwoNumbers.split())
multiplicationResult = num1 * num2
print("The multiplication of", num1, "and", num2, "is:", multiplicationResult)
# This code prompts the user to enter two numbers, calculates their product, and then displays the result.