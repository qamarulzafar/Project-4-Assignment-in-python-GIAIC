# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.



user_1 = int(input("Enter a Number : "))
user_2 = int(input("Enter a second number : "))

def calculate_sum (num1 , num2):
    sum = num1 + num2
    return sum


result =  calculate_sum(user_1,user_2)
print(f"The Sum of Two Number is {result}")

