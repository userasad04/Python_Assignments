# =========================
# File Handling in Python
# =========================

# -------------------------
# Example 1: Reading from a file
# -------------------------
try:
    with open("HW.txt", "r") as file1:  # using 'with' ensures file is closed automatically
        data = file1.read()
        print("Contents of HW.txt:\n", data)
except FileNotFoundError:
    print("HW.txt not found!")
print()

# -------------------------
# Example 2: Writing to a file
# -------------------------
try:
    with open("Blank.txt", "w") as file2:
        str1 = 'My name is Syed Asad and I am a programmer'
        file2.write(str1)
        print("Written to Blank.txt successfully")
except Exception as e:
    print("Error writing to file:", e)
print()

# -------------------------
# Example 3: Reading and updating a file
# -------------------------
try:
    with open("HW.txt", "r+") as file3:
        line = file3.readline(11)  # read first 11 characters
        print("First 11 characters of HW.txt:", line)
except FileNotFoundError:
    print("HW.txt not found!")
