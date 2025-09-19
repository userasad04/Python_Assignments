# =========================
# Different Ways to Create Strings
# =========================
string1 = 'Hello'
print(string1)

string2 = "Hello"
print(string2)

string3 = '''World'''
print(string3)

string4 = """Welcome to
the world of Python"""  # Triple quotes can extend multiple lines
print(string4)
print()

# =========================
# Concatenating Strings
# =========================
concatenated = string1 + string3
print("Concatenated two different strings:", concatenated)
print()

# =========================
# Finding the Length of a String
# =========================
print("Length of the concatenated string:", len(concatenated))
print()

# =========================
# Extracting Substrings and Searching
# =========================
str_main = 'kashish'
substr1 = 'ish'
substr2 = 'h'

print("Position of 'ish':", str_main.index(substr1))
print("Position of 'h':", str_main.index(substr2))
print()

# =========================
# Matching a String Using Regular Expressions
# =========================
import re

pattern = 'Madara'
text = 'Madara once said- Wake up to reality, nothing goes as planned in this cursed world'

# re.match() checks if the pattern matches the beginning of the string
match_result = re.match(pattern, text)
print("Regex match result:", match_result)
print()

# =========================
# Comparing Strings
# =========================
str_a = 'Itachi Uchiha'
str_b = 'Madara Uchiha'
str_c = str_a

print(str_a == str_b)  # False
print(str_a == str_c)  # True
print(str_b == str_c)  # False
print(str_a != str_b)  # True
print()

# =========================
# startswith() and endswith()
# =========================
name = 'Minato Namikaze'
print(name.startswith("Minato"))  # True
print(name.endswith("kaze"))      # True
print()

# =========================
# Trimming Strings with strip()
# =========================
trimmed = '  Hello World hi  '
print(trimmed.strip())           # Removes leading/trailing spaces
print(trimmed.strip("hi "))      # Removes specific characters from ends
print()

# =========================
# Replacing Characters in Strings
# =========================
greeting = 'Hi World'
print(greeting.replace("Hi", "Hello"))
print()

# =========================
# Splitting Strings
# =========================
str_to_split = 'hi-hello-bye'
print(str_to_split.split("-"))
print()

# =========================
# Converting Integers to Strings
# =========================
num = 10
num_str = str(num)
print(num_str)
print(type(num_str))
print()

# =========================
# Converting to Uppercase and Lowercase
# =========================
lower_str = 'hello'
upper_str = 'WORLD'

print(lower_str.upper())
print(upper_str.lower())
