# =========================
# Arithmetic Operators
# =========================
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else 'Undefined (division by zero)'

print('The sum of {} and {} is {}'.format(num1, num2, sum_result))
print('The subtraction of {} and {} is {}'.format(num1, num2, sub_result))
print('The multiplication of {} and {} is {}'.format(num1, num2, mul_result))
print('The division of {} and {} is {}'.format(num1, num2, div_result))
print()

# =========================
# Increment and Decrement
# =========================
a = 0
a += 1   # Increment by 1
a = a + 1
print('The value of a after incrementing twice:', a)

print("\nINCREMENTED FOR LOOP")
for i in range(0, 5):  # 0 to 4
    print(i)

print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):  # 4 to 0
    print(i)
print()

# =========================
# Check if Two Numbers are Equal
# =========================
a = input('Enter first number: ')
b = input('Enter second number: ')

if a == b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
print()

# =========================
# Relational Operators
# =========================
a = 4
b = 5

print("a < b:", a < b)
print("a <= b:", a <= b)
print("a > b:", a > b)
print("a >= b:", a >= b)
print("a == b:", a == b)
print("a != b:", a != b)
print()

# =========================
# Find Smaller and Larger Number
# =========================
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")

if a < b:
    print(a, "is smaller")
else:
    print(b, "is smaller")
