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
    # Example for uppercase
    print("Uppercase conversion:", demonstrate_uppercase("Computer Science and Engineering"))
    # Example for lowercase
    print("Lowercase conversion:", demonstrate_lowercase("Computer Science and Engineering"))
    # Example for swapcase
    print("Swapped case:", demonstrate_swapcase("Computer Science and Engineering"))
    # Example for union
    print("Union of sets:", demonstrate_union({1, 2, 3, 4, 6}, {3, 4, 5}))
    # Example for reverse string
    print("Reversed string:", demonstrate_reverse_string("Computer Science and Engineering"))
    # Example for round
    print("Rounded number (to 3 decimal places):", demonstrate_round(3.14159, 3))
    # Example for sum
    print("Sum of numbers:", demonstrate_sum([1, 2, 3, 4, 5]))
    # Example for subtraction
    print("Subtraction of numbers (10 - 5):", demonstrate_subtraction(10, 5))
    # Example for product
    print("Product of numbers:", demonstrate_product([1, 2, 3, 4, 5]))
    # Example for division
    print("Division of numbers (10 / 2):", demonstrate_division(10, 2))
    # Example for find and replace
    print("Find and replace 'Engineering' with 'Art':", demonstrate_find_replace("Computer Science and Engineering", "Engineering", "Art"))

# Run the main function
if __name__ == "__main__":
    main()
    
