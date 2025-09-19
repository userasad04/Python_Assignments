# =========================
# Static Variables in Python
# =========================

class Python:
    # Static (class) variable
    staticVariable = 9

# -------------------------
# Access static variable through class
# -------------------------
print("Access through class:", Python.staticVariable)

# -------------------------
# Modify static variable through class
# -------------------------
Python.staticVariable = 12
print("After changing through class:", Python.staticVariable)

# -------------------------
# Access static variable through an instance
# -------------------------
instance = Python()
print("Access through instance:", instance.staticVariable)

# -------------------------
# Change static variable through instance
# -------------------------
instance.staticVariable = 15  # This creates an instance variable, doesn't change class variable
print("After changing through instance:", instance.staticVariable)  
print("Class variable remains unchanged:", Python.staticVariable)
