# 1) Add integer values of an array
def sum_array(arr):
    return sum(arr)

print("Sum:", sum_array([10, 20, 30, 40]))

# 2) Average value of array
def average_array(arr):
    return sum(arr) / len(arr)

print("Average:", average_array([10, 21, 32, 43, 54]))

# 3) Index of array element
arr = [1, 3, 5, 3, 1, 2, 6, 5, 3, 8, 6, 9]
print("Index of 3:", arr.index(3))
print("Index of 9:", arr.index(9))

# 4) Check if array contains specific value
arr = [4, 5, 45, 40, 50]
print("Contains 5:", 5 in arr)

# 5) Remove specific element
arr = [44, 55, 0, 15, 19, 5, 4]
arr.remove(0)
print("After removal:", arr)

# 6) Copy an array
arr = ['a','s','a','d']
arr1 = arr.copy()
print("Copied array:", arr1)

# 7) Insert element at specific position
arr = [101, 303, 404]
arr.insert(1, 202)
print("After insert:", arr)

# 8) Min and Max values
arr = [100, 3, 3000, 20, 500]
print("Min:", min(arr), "Max:", max(arr))

# 9) Reverse array
arr = [9, 8, 7, 6, 5]
arr.reverse()
print("Reversed:", arr)

# 10) Find duplicates
arr = [21, 11, 31, 13, 11]
duplicates = [x for i, x in enumerate(arr) if x in arr[:i]]
print("Duplicates:", set(duplicates))

# 11) Common values between arrays
arr1 = ['a','s','a','d']
arr2 = ['s','h','a']
print("Common:", set(arr1) & set(arr2))

# 12) Remove duplicates
arr = [11, 22, 33, 11, 44, 55]
print("Without duplicates:", list(set(arr)))

# 13) Second largest number
arr = [101, 404, 202, 909, 606]
print("Second largest:", sorted(set(arr))[-2])

# 14) Count even and odd
arr = [1,2,3,4,5,6,7,8,9]
evens = sum(1 for x in arr if x % 2 == 0)
odds = len(arr) - evens
print("Even:", evens, "Odd:", odds)

# 15) Difference between largest and smallest
arr = [10, 6, 11, 13, 14]
print("Difference:", max(arr) - min(arr))

# 16) Verify if array contains elements 12 and 23
arr = [1, 12, 19, 23, 33, 54]
print("Contains 12 and 23:", 12 in arr and 23 in arr)
