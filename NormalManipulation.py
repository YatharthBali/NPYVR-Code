import math
# Function to demonstrate converting to uppercase
def demonstrate_uppercase(text):
    return text.upper()
# Function to demonstrate converting to lowercase
def demonstrate_lowercase(text):
    return text.lower()
# Function to demonstrate swapcase()
def demonstrate_swapcase(text):
    return text.swapcase()
# Function to demonstrate union() on sets
def demonstrate_union(set1, set2):
    return set1 | set2
# Function to demonstrate reversing a string
def demonstrate_reverse_string(text):
    return text[::-1]
# Function to demonstrate round()
def demonstrate_round(number, digits):
    return round(number, digits)
# Function to demonstrate sum()
def demonstrate_sum(numbers):
    return sum(numbers)
# Function to demonstrate subtraction
def demonstrate_subtraction(a, b):
    return a - b
# Function to demonstrate product() using math.prod()
def demonstrate_product(numbers):
    return math.prod(numbers)
# Function to demonstrate division
def demonstrate_division(a, b):
    if b == 0:
        return "Division by zero is undefined"
    return a / b
# Function to demonstrate find and replace in a string
def demonstrate_find_replace(text, old, new):
    return text.replace(old, new)

# Main function to show examples
def main():
    while True:
        operation = input("Enter operation (uppercase, lowercase, swapcase, union, reverse, round, sum, subtraction, product, division), or type 'reset' to choose another operation: ").lower()

        if operation == "reset":
            continue
        elif operation == "uppercase":
            text = input("Enter text: ")
            print("Uppercase conversion:", demonstrate_uppercase(text))
        elif operation == "lowercase":
            text = input("Enter text: ")
            print("Lowercase conversion:", demonstrate_lowercase(text))
        elif operation == "swapcase":
            text = input("Enter text: ")
            print("Swapped case:", demonstrate_swapcase(text))
        elif operation == "union":
            set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
            set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))
            print("Union of sets:", demonstrate_union(set1, set2))
        elif operation == "reverse":
            text = input("Enter text: ")
            print("Reversed string:", demonstrate_reverse_string(text))
        elif operation == "round":
            number = float(input("Enter number: "))
            digits = int(input("Enter number of digits: "))
            print("Rounded number:", demonstrate_round(number, digits))
        elif operation == "sum":
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Sum of numbers:", demonstrate_sum(numbers))
        elif operation == "subtraction":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Subtraction:", demonstrate_subtraction(a, b))
        elif operation == "product":
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Product of numbers:", demonstrate_product(numbers))
        elif operation == "division":
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print("Division:", demonstrate_division(a, b))
        else:
            print("Invalid operation!")

        choice = input("Do you want to perform another operation? (yes/no): ").lower()
        if choice != "yes":
            break

# Run the main function
if __name__ == "__main__":
    main()
