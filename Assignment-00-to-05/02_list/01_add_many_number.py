# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_numbers(numbers) -> int:

    total_so_far:int = 0 
    for number in numbers:
        total_so_far += number


    return total_so_far


print(add_many_numbers([1,2,4,5,5]))


def main():
    numbers:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_of_numbers: int = add_many_numbers(numbers)
    print(sum_of_numbers)


main()