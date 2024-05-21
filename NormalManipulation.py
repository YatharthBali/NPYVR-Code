import argparse

def reverse(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        reversed_text = text[::-1]
        print(f"Reversed text:\n{reversed_text}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_and_replace(file_path, find_word, replace_word):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.replace(find_word, replace_word)
        with open(file_path, 'w') as file:
            file.write(new_text)
        print(f"Replaced all occurrences of '{find_word}' with '{replace_word}'.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def swap_case(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.swapcase()
        with open(file_path, 'w') as file:
            file.write(new_text)
        print("Swapped case of all text.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        num_words = len(words)
        print(f"Number of words in the text: {num_words}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_uppercase(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.upper()
        with open(file_path, 'w') as file:
            file.write(new_text)
        print("Converted all text to uppercase.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_lowercase(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.lower()
        with open(file_path, 'w') as file:
            file.write(new_text)
        print("Converted all text to lowercase.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_and_count_vowels_consonants(file_path):
    vowels = "aeiouAEIOU"
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        num_vowels = sum(1 for char in text if char in vowels)
        num_consonants = sum(1 for char in text if char.isalpha() and char not in vowels)
        print(f"Number of vowels in the text: {num_vowels}")
        print(f"Number of consonants in the text: {num_consonants}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Text Manipulation Utility")

    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Sub-parser for reverse
    parser_reverse = subparsers.add_parser('reverse', help='Reverse the content of a text file')
    parser_reverse.add_argument('file', type=str, help='Path to the text file')

    # Sub-parser for find and replace
    parser_replace = subparsers.add_parser('replace', help='Find and replace text in a file')
    parser_replace.add_argument('file', type=str, help='Path to the text file')
    parser_replace.add_argument('find', type=str, help='Word to find')
    parser_replace.add_argument('replace', type=str, help='Word to replace with')

    # Sub-parser for case swapping
    parser_swap = subparsers.add_parser('swapcase', help='Swap case of all text in a file')
    parser_swap.add_argument('file', type=str, help='Path to the text file')

    # Sub-parser for word count
    parser_count = subparsers.add_parser('wordcount', help='Count the number of words in a file')
    parser_count.add_argument('file', type=str, help='Path to the text file')

    # Sub-parser for converting to uppercase
    parser_uppercase = subparsers.add_parser('uppercase', help='Convert all text to uppercase')
    parser_uppercase.add_argument('file', type=str, help='Path to the text file')

    # Sub-parser for converting to lowercase
    parser_lowercase = subparsers.add_parser('lowercase', help='Convert all text to lowercase')
    parser_lowercase.add_argument('file', type=str, help='Path to the text file')

    # Sub-parser for finding and counting vowels and consonants
    parser_find_count_vc = subparsers.add_parser('countvc', help='Count the number of vowels and consonants in a file')
    parser_find_count_vc.add_argument('file', type=str, help='Path to the text file')

    args = parser.parse_args()

    if args.command == 'reverse':
        reverse(args.file)
    elif args.command == 'replace':
        find_and_replace(args.file, args.find, args.replace)
    elif args.command == 'swapcase':
        swap_case(args.file)
    elif args.command == 'wordcount':
        count_words(args.file)
    elif args.command == 'uppercase':
        convert_to_uppercase(args.file)
    elif args.command == 'lowercase':
        convert_to_lowercase(args.file)
    elif args.command == 'countvc':
        find_and_count_vowels_consonants(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
