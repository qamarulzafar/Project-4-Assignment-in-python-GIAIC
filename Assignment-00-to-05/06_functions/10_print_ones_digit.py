# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2


def print_ones_digit(num):
    once_digit = num % 10 
    print(f"The Once Digit is {once_digit}")


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

main()