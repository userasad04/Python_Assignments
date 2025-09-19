# 1) Print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

# 2) Print 1 to 20 numbers using while loop
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print("\n")

# 3) Equal and not equal operators
a, b = 5, 10
print("a == b:", a == b)
print("a != b:", a != b)

# 4) Print odd and even numbers from a list
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even Numbers:", [n for n in Numbers if n % 2 == 0])
print("Odd Numbers:", [n for n in Numbers if n % 2 != 0])

# 5) Largest among three numbers
x, y, z = 40, 50, 90
largest = max(x, y, z)
print(x,y,z)
print("Largest number is:", largest)

# 6) Print even numbers between 10 and 20 using while
a, b = 10, 20
print("Even numbers between 10 and 20:", end=" ")
while a <= b:
    if a % 2 == 0:
        print(a, end=" ")
    a += 1
print("\n")

# 7) Do-while loop simulation (print 1 to 10)
a = 1
print("Numbers 1 to 10 using simulated do-while:", end=" ")
while True:
    print(a, end=" ")
    a += 1
    if a > 10:
        break
print("\n")

# 8) Armstrong number check (works for any digit length)
num = int(input("Enter a number to check Armstrong or not: "))
temp = num
power = len(str(num))
sum_of_digits = 0

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** power
    temp //= 10

if num == sum_of_digits:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 9) Prime number check
number = int(input("Enter a number to check prime or not: "))
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# 10) Palindrome number check
n = int(input("Enter a number to check palindrome: "))
temp, rev = n, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not a palindrome")

# 11) Check even or odd
n = int(input("Enter a number to check EVEN/ODD: "))
print(f"{n} is Even" if n % 2 == 0 else f"{n} is Odd")
