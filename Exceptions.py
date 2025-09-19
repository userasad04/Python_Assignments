# =========================
# Exceptions in Python
# =========================

# -------------------------
# Example 1: Handling IndexError
# -------------------------
a = [1, 2, 3]

try:
    print("Second element =", a[1])
    
    # This will throw an IndexError
    print("Fourth element =", a[3])
except IndexError:
    print("An error occurred: Index out of range")
print()

# -------------------------
# Example 2: Using else with try-except
# -------------------------
b = [3, 2, 1]

try:
    if a == b:
        print("Both lists are equal")
    else:
        raise ValueError("Lists are not equal")  # manually raise exception
except ValueError as ve:
    print(ve)
else:
    print("No exception, lists are equal")
print()

# -------------------------
# Example 3: ZeroDivisionError and finally
# -------------------------
try:
    k = 5 / 0  # This will raise ZeroDivisionError
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This block is always executed")
