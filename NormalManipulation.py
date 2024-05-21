import argparse
import sys

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        print(f"Word Count: {len(words)}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def RePlace(file_path, find_word, replace_word):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.replace(find_word, replace_word) #here it is finding oldword,newWord
        with open(file_path, 'w') as file:
            file.write(new_text)
        print(f"Replaced all occurrences of '{find_word}' with '{replace_word}'.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_case(file_path, to_upper):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        new_text = text.upper() if to_upper else text.lower()
        with open(file_path, 'w') as file:
            file.write(new_text)
        print(f"Converted text to {'uppercase' if to_upper else 'lowercase'}.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Text Manipulation Utility")
    
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')
    
    # Sub-parser for word count
    parser_count = subparsers.add_parser('count', help='Count words in a text file')
    parser_count.add_argument('file', type=str, help='Path to the text file')
    
    # Sub-parser for find and replace
    parser_replace = subparsers.add_parser('replace', help='Find and replace text in a file')
    parser_replace.add_argument('find', type=str, help='Word to find')
    parser_replace.add_argument('replace', type=str, help='Word to replace with')
    
    # Sub-parser for case conversion
    parser_case = subparsers.add_parser('case', help='Convert text case')
    parser_case.add_argument('file', type=str, help='Path to the text file')
    parser_case.add_argument('--upper', action='store_true', help='Convert text to uppercase')
    parser_case.add_argument('--lower', action='store_true', help='Convert text to lowercase')
    
    args = parser.parse_args()

    if args.command == 'count':
        count_words(args.file)
    elif args.command == 'replace':
        RePlace(args.file, args.find, args.replace)
    elif args.command == 'case':
        if args.upper == args.lower:
            print("Error: Specify either --upper or --lower.")
            sys.exit(1)
        convert_case(args.file, args.upper)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
