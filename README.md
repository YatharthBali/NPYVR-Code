Text Manipulation Utility
Introduction
The Text Manipulation Utility is a versatile Python script designed to perform various text operations on files. It supports reversing text, finding and replacing words, case manipulation, counting words, sorting lines, and more. This utility is ideal for users who need to automate text processing tasks in a simple and efficient manner.

Requirements
To run this script, you need the following:

Python 3.6 or higher
argparse library (included in the standard Python library)
Features
The Text Manipulation Utility provides the following functionalities:

Reverse Text: Reverse the entire content of a text file.
Find and Replace: Find a specific word in the file and replace it with another word.
Swap Case: Swap the case of all characters in the file (uppercase to lowercase and vice versa).
Count Words: Count the number of words in the file.
Convert to Uppercase: Convert all text in the file to uppercase.
Convert to Lowercase: Convert all text in the file to lowercase.
Count Vowels and Consonants: Count the number of vowels and consonants in the file.
Find Vowels and Consonants: List all vowels and consonants found in the file.
Sort Lines: Sort the characters in each line of the file alphabetically.
Split Lines: Split the characters in each line of the file with a space between them.
Functions
reverse(file_path)
Reverses the entire content of the specified file and prints it.

find_and_replace(file_path, find_word, replace_word)
Finds all occurrences of find_word in the file and replaces them with replace_word.

swap_case(file_path)
Swaps the case of all characters in the file and prints the result.

count_words(file_path)
Counts and prints the number of words in the file.

convert_to_uppercase(file_path)
Converts all characters in the file to uppercase and overwrites the file.

convert_to_lowercase(file_path)
Converts all characters in the file to lowercase and overwrites the file.

find_and_count_vowels_consonants(file_path)
Counts and prints the number of vowels and consonants in the file.

find_vowels_and_consonants(file_path)
Lists and prints all vowels and consonants found in the file.

sort_lines(file_path)
Sorts the characters in each line of the file alphabetically and overwrites the file.

split_lines(file_path)
Splits the characters in each line with a space between them and prints the result.

Usage
To use this utility, you need to run the script with the desired command and file path. Here are the available commands and their usage:

bash
Copy code
python script_name.py reverse <file_path>
python script_name.py replace <file_path> <find_word> <replace_word>
python script_name.py swapcase <file_path>
python script_name.py wordcount <file_path>
python script_name.py uppercase <file_path>
python script_name.py lowercase <file_path>
python script_name.py countvc <file_path>
python script_name.py vc <file_path>
python script_name.py sorting <file_path>
python script_name.py splitting <file_path>
Example Usage
Reverse the content of a file:

bash
Copy code
python script_name.py reverse example.txt
Find and replace a word:

bash
Copy code
python script_name.py replace example.txt old_word new_word
Swap case of all characters:

bash
Copy code
python script_name.py swapcase example.txt
Count the number of words:

bash
Copy code
python script_name.py wordcount example.txt
Convert text to uppercase:

bash
Copy code
python script_name.py uppercase example.txt
Convert text to lowercase:

bash
Copy code
python script_name.py lowercase example.txt
Count vowels and consonants:

bash
Copy code
python script_name.py countvc example.txt
Find vowels and consonants:

bash
Copy code
python script_name.py vc example.txt
Sort characters in each line:

bash
Copy code
python script_name.py sorting example.txt
Split characters in each line:

bash
Copy code
python script_name.py splitting example.txt
Error Handling
The script includes error handling for common issues such as file not found and I/O errors, ensuring that informative error messages are printed to guide the user.

Contributors
This Text Manipulation Utility was developed by the following contributors:

Yatharth
Bhumireddy Vanitha
Parsanna
Rutuja
Nikhil Choudhary
Conclusion
This Text Manipulation Utility is a powerful tool for performing a variety of text operations on files. It is easy to use, with each function designed to handle specific text manipulation tasks efficiently. Whether you need to reverse text, count words, or manipulate case, this script has you covered.
