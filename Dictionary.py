# =========================
# Dictionary Operations in Python
# =========================

# -------------------------
# Creating a dictionary
# -------------------------
Dict = dict([(1, 'Syed Asad'), (2, 'Kritika'), (3, 'Aastha'), (4, 'Vaishali'), (5, 'Muskan')])
print("Dictionary with each item as a pair:", Dict)

# -------------------------
# Adding an element to dictionary
# -------------------------
Dict[6] = 'Nitya'
print("\nDictionary with new item added:", Dict)

# -------------------------
# Updating values in dictionary
# -------------------------
Dict[3] = 'Navdisha'
print("\nDictionary with updated value:", Dict)

# -------------------------
# Accessing a value in dictionary
# -------------------------
print("\nAccessing value for key 1:", Dict[1])

# -------------------------
# Deleting a value from dictionary
# -------------------------
del Dict[6]
print("\nDictionary after deleting key 6:", Dict)

# -------------------------
# Creating a nested dictionary
# -------------------------
Dict1 = {
    1: 'Syed Asad',
    2: 'Kritika',
    3: {'Age': 18, 'Branch': 'CSE', 'Year': 'Third Year'}
}
print("\nNested dictionary:", Dict1)

# Accessing an element of a nested dictionary
print("\nAccessing element for key 3 in nested dictionary:", Dict1[3])
