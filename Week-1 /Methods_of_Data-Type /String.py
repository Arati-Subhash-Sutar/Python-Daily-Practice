# indexing

# Q1: WAP to get the first character of a string
s = "python"
print(s[0])
# Q2: WAP to get the last character of a string using positive index
s = "python"
print(s[5])
# Q3: WAP to get the character at index 3
s = "learning"
print(s[3])
# Q4: WAP to get the second last character using negative index
s = "python"
print(s[-2])
# Q5: WAP to get the first character using negative index
s = "python"
print(s[-6])


# slicing

# Q1: WAP to extract the first three characters of a string
s = "python"
print(s[0:3])
# Q2: WAP to extract characters from index 2 to the end
s = "python"
print(s[2:])
# Q3: WAP to extract the middle portion of a string
s = "programming"
print(s[3:7])
# Q4: WAP to reverse a string using slicing step
s = "python"
print(s[::-1])
# Q5: WAP to extract every second character from a string
s = "python"
print(s[::2])


# upper

# Q1: WAP to convert a word to uppercase
s = "hello"
print(s.upper())
# Q2: WAP to convert a sentence to uppercase
s = "python is fun"
print(s.upper())
# Q3: WAP to convert a single character to uppercase
s = "a"
print(s.upper())
# Q4: WAP to convert mixed text to uppercase
s = "Code123"
print(s.upper())

# lower

# Q1: WAP to convert an uppercase word to lowercase
s = "HELLO"
print(s.lower())
# Q2: WAP to convert a sentence to lowercase
s = "PYTHON IS FUN"
print(s.lower())
# Q3: WAP to convert a single capital letter to lowercase
s = "Z"
print(s.lower())
# Q4: WAP to convert mixed text to lowercase
s = "CoDe"
print(s.lower())

# swapcase

# Q1: WAP to swap cases of a simple word
s = "Python"
print(s.swapcase())
# Q2: WAP to swap cases of an all caps word
s = "HELLO"
print(s.swapcase())
# Q3: WAP to swap cases of a lowercase word
s = "world"
print(s.swapcase())
# Q4: WAP to swap cases in a mixed string
s = "PyThOn"
print(s.swapcase())

# capitalize

# Q1: WAP to capitalize a lowercase word
s = "python"
print(s.capitalize())
# Q2: WAP to capitalize a full lowercase sentence
s = "learning python is easy"
print(s.capitalize())
# Q3: WAP to fix an all caps word using capitalize
s = "PYTHON"
print(s.capitalize())
# Q4: WAP to capitalize a single letter
s = "a"
print(s.capitalize())

# title

# Q1: WAP to convert a sentence into title case
s = "python programming language"
print(s.title())
# Q2: WAP to title case a person's name
s = "john doe"
print(s.title())
# Q3: WAP to title case words separated by spaces
s = "welcome to code"
print(s.title())
# Q4: WAP to title case a mix of words
s = "hello world python"
print(s.title())

# islower

# Q1: WAP to check if a word is entirely lowercase
s = "python"
print(s.islower())
# Q2: WAP to check if an uppercase word is lowercase
s = "Python"
print(s.islower())
# Q3: WAP to check if a lowercase sentence is lowercase
s = "hello world"
print(s.islower())
# Q4: WAP to check if numbers with text are lowercase
s = "abc123"
print(s.islower())

# isupper

# Q1: WAP to check if a word is entirely uppercase
s = "PYTHON"
print(s.isupper())
# Q2: WAP to check if a lowercase word is uppercase
s = "python"
print(s.isupper())
# Q3: WAP to check if an uppercase sentence is uppercase
s = "HELLO WORLD"
print(s.isupper())
# Q4: WAP to check if mixed text is uppercase
s = "PYTHON3"
print(s.isupper())

# isspace

# Q1: WAP to check if a string contains only spaces
s = "   "
print(s.isspace())
# Q2: WAP to check if a tab character string is space
s = "\t"
print(s.isspace())
# Q3: WAP to check if a normal word is space
s = "hello"
print(s.isspace())
# Q4: WAP to check if a newline character is space
s = "\n"
print(s.isspace())

# isdigit

# Q1: WAP to check if a string contains only digits
s = "12345"
print(s.isdigit())
# Q2: WAP to check if a number with letters is digit
s = "123a"
print(s.isdigit())
# Q3: WAP to check if a single digit string is digit
s = "7"
print(s.isdigit())
# Q4: WAP to check if a decimal string is digit
s = "12.34"
print(s.isdigit())

# isalnum

# Q1: WAP to check if a string is alphanumeric
s = "Python123"
print(s.isalnum())
# Q2: WAP to check if letters only string is alphanumeric
s = "Python"
print(s.isalnum())
# Q3: WAP to check if numbers only string is alphanumeric
s = "123"
print(s.isalnum())
# Q4: WAP to check if a string with special characters is alphanumeric
s = "Python_123"
print(s.isalnum())

# count

# Q1: WAP to count character occurrences in a string
s = "banana"
print(s.count("a"))
# Q2: WAP to count a letter in a word
s = "python"
print(s.count("p"))
# Q3: WAP to count a substring in a sentence
s = "apple banana apple"
print(s.count("apple"))
# Q4: WAP to count a missing letter in a string
s = "hello"
print(s.count("z"))

# index

# Q1: WAP to find the index of a character
s = "python"
print(s.index("t"))
# Q2: WAP to find the index of the first letter
s = "python"
print(s.index("p"))
# Q3: WAP to find the index of a substring
s = "learning"
print(s.index("arn"))
# Q4: WAP to find the index of a character in a sentence
s = "hello world"
print(s.index("o"))

# rindex

# Q1: WAP to find the last index of a character
s = "banana"
print(s.rindex("a"))
# Q2: WAP to find the last index of a repeating letter
s = "python"
print(s.rindex("p"))
# Q3: WAP to find the last index of a substring
s = "hello hello"
print(s.rindex("hello"))
# Q4: WAP to find the last index of a character in a sentence
s = "programming"
print(s.rindex("g"))

# find

# Q1: WAP to find a character position using find
s = "python"
print(s.find("t"))
# Q2: WAP to find a substring position
s = "learning python"
print(s.find("python"))
# Q3: WAP to find a character that is absent
s = "python"
print(s.find("z"))
# Q4: WAP to find the first character position
s = "python"
print(s.find("p"))

# rfind

# Q1: WAP to find the last position of a character
s = "banana"
print(s.rfind("a"))
# Q2: WAP to find the last position of a substring
s = "test test test"
print(s.rfind("test"))
# Q3: WAP to find an absent character using rfind
s = "hello"
print(s.rfind("z"))
# Q4: WAP to find the last position of a letter
s = "python"
print(s.rfind("o"))

# join

# Q1: WAP to join characters of a string with a space
s = "python"
print(" ".join(s))
# Q2: WAP to join characters of a string with a hyphen
s = "code"
print("-".join(s))
# Q3: WAP to join characters of a string with an underscore
s = "hello"
print("_".join(s))
# Q4: WAP to join characters of a string with a custom symbol
s = "java"
print("*".join(s))


# split

# Q1: WAP to split a sentence by space
s = "python is fun"
print(s.split())
# Q2: WAP to split a CSV string by comma
s = "apple,banana,cherry"
print(s.split(","))
# Q3: WAP to split words by a hyphen
s = "one-two-three"
print(s.split("-"))
# Q4: WAP to split a string by a specific letter
s = "banana"
print(s.split("n"))

# replace

# Q1: WAP to replace a word in a sentence
s = "I like cats"
print(s.replace("cats", "dogs"))
# Q2: WAP to replace a character in a string
s = "hello"
print(s.replace("l", "z"))
# Q3: WAP to remove spaces by replacing them with empty string
s = "p y t h o n"
print(s.replace(" ", ""))
# Q4: WAP to replace a substring
s = "python 2"
print(s.replace("2", "3"))


# strip

# Q1: WAP to remove leading and trailing spaces
s = "   python   "
print(s.strip())
# Q2: WAP to remove custom characters from both ends
s = "###hello###"
print(s.strip("#"))
# Q3: WAP to remove newlines and spaces from ends
s = "\n  hello  \n"
print(s.strip())
# Q4: WAP to strip specific letters from both ends
s = "xxhellowx"
print(s.strip("x"))


# rstrip

# Q1: WAP to remove trailing spaces from a string
s = "python   "
print(s.rstrip())
# Q2: WAP to remove trailing custom characters
s = "hello!!!"
print(s.rstrip("!"))
# Q3: WAP to remove trailing newlines
s = "hello\n"
print(s.rstrip())
# Q4: WAP to remove trailing specific letters
s = "hellommm"
print(s.rstrip("m"))


# lstrip

# Q1: WAP to remove leading spaces from a string
s = "   python"
print(s.lstrip())
# Q2: WAP to remove leading custom characters
s = "###hello"
print(s.lstrip("#"))
# Q3: WAP to remove leading newlines
s = "\nhello"
print(s.lstrip())
# Q4: WAP to remove leading specific letters
s = "xxhello"
print(s.lstrip("x"))

# startswith

# Q1: WAP to check if a string starts with a prefix
s = "python"
print(s.startswith("py"))
# Q2: WAP to check if a file name starts with a word
s = "report.txt"
print(s.startswith("rep"))
# Q3: WAP to check startswith with wrong prefix
s = "python"
print(s.startswith("java"))
# Q4: WAP to check startswith using a single character
s = "hello"
print(s.startswith("h"))


# endswith

# Q1: WAP to check if a file ends with an extension
s = "script.py"
print(s.endswith(".py"))
# Q2: WAP to check if a string ends with a suffix
s = "python"
print(s.endswith("on"))
# Q3: WAP to check endswith with wrong suffix
s = "python"
print(s.endswith("java"))
# Q4: WAP to check endswith using a single character
s = "hello"
print(s.endswith("o"))


# removeprefix

# Q1: WAP to remove a URL protocol prefix
s = "https://example.com"
print(s.removeprefix("https://"))
# Q2: WAP to remove a file prefix
s = "pre_data.txt"
print(s.removeprefix("pre_"))
# Q3: WAP to remove a non-matching prefix safely
s = "python"
print(s.removeprefix("java"))
# Q4: WAP to remove a short prefix from a word
s = "unhappy"
print(s.removeprefix("un"))


# removesuffix

# Q1: WAP to remove a file extension suffix
s = "image.png"
print(s.removesuffix(".png"))
# Q2: WAP to remove a text suffix
s = "filename_old"
print(s.removesuffix("_old"))
# Q3: WAP to remove a non-matching suffix safely
s = "python"
print(s.removesuffix("java"))
# Q4: WAP to remove a short suffix from a word
s = "testing"
print(s.removesuffix("ing"))
