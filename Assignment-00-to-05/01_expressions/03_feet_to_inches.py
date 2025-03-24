# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.



inches_in_foot: int = 12

def main():
    feet : float = float(input("Enter Number Of Feet: "))
    inches: float = feet * inches_in_foot
    print("This is ", inches, "inches")

main()
