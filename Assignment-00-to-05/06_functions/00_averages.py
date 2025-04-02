# Write a function that takes two numbers and finds the average between the two



def average(num1: float, num2: float):

    sum = num1 + num2
    return sum / 2


def main():
    avg_1 = average(5, 10)
    avg_2 = average(15, 20)

    print(f"Average of 5 and 10 is: {avg_1}")
    print(f"Average of 15 and 20 is: {avg_2}")


if __name__ == "__main__":
    main()








