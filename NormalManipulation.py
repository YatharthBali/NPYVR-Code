import math
# Function to demonstrate swapcase()
def demonstrate_swapcase(text):
    return text.swapcase()
# Function to demonstrate union() on sets
def demonstrate_union(set1, set2):
    return set1 | set2
# Function to demonstrate round()
def demonstrate_round(number, digits):
    return round(number, digits)
# Function to demonstrate sum()
def demonstrate_sum(numbers):
    return sum(numbers)
# Function to demonstrate product() using math.prod()
def demonstrate_product(numbers):
    return math.prod(numbers)
# Function to demonstrate subtraction
def demonstrate_subtraction(a, b):
    return a - b
# Function to demonstrate division
def demonstrate_division(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
# Main function to show examples
def main():
    # Example for swapcase()
    print("Swapped case:", demonstrate_swapcase("Computer Science and Engineering"))
        # Example for union()
    print("Union of sets:", demonstrate_union({1, 2, 3}, {3, 4, 5}))
        # Example for round()
    print("Rounded number (to 3 decimal places):", demonstrate_round(3.14159, 3))
        # Example for sum()
    print("Sum of numbers:", demonstrate_sum([1, 2, 3, 4, 5]))
       # Example for product()
    print("Product of numbers:", demonstrate_product([1, 2, 3, 4, 5]))
    # Example for subtraction
    print("Subtraction (10 - 5):", demonstrate_subtraction(10, 5))
    # Example for division
    print("Division (10 / 2):", demonstrate_division(10, 2))
    print("Division (10 / 0):", demonstrate_division(10, 0))
# Run the main function
if __name__ == "__main__":
    main()

