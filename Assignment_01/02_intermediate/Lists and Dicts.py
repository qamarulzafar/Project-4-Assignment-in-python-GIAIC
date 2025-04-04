def access_element(lst, index):
    if index < len(lst):
        return lst[index]
    else:
        return "Index out of range"
    

def modify_element(lst, index, new_value):
    if index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range"
    

def slice_list(lst, start, end):
    return lst[start:end]


def index_game():
    my_list = ['cheery', 'banana', 'orange', 'apple', 'kiwi']
    print("Here is the current list:", my_list)

    print("What would you like to do? (access / modify / slice)")
    operation = input("Enter operation: ").lower()

    if operation == "access":
        index = int(input("Which index do you want to access? "))
        print("Result:", access_element(my_list, index))

    elif operation == "modify":
        index = int(input("Which index do you want to modify? "))
        new_value = input("What will be the new value? ")
        print("Updated List:", modify_element(my_list, index, new_value))

    elif operation == "slice":
        start = int(input("Start index: "))
        end = int(input("End index: "))
        print("Sliced List:", slice_list(my_list, start, end))

    else:
        print("Invalid operation. Please choose: access, modify, or slice.")


index_game()
