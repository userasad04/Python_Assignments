# =========================
# Inheritance in Python
# =========================

# -------------------------
# Base Class
# -------------------------
class A:
    def display(self):
        print("Display inside class A")
    
    def show(self):
        print("Show inside class A")


# -------------------------
# Subclass B inheriting from A
# -------------------------
class B(A):
    def print_method(self):
        print("Print inside class B")
    
    def show(self):  # Overrides show() from class A
        print("Show inside class B")


# -------------------------
# Subclass C inheriting from B
# -------------------------
class C(B):
    def show(self):  # Overrides show() from class B
        print("Show inside class C")


# -------------------------
# Driver Code
# -------------------------
# Object of Base Class A
obj_a = A()
obj_a.display()  # Calls A.display()
obj_a.show()     # Calls A.show()
print()

# Object of Subclass B
obj_b = B()
obj_b.display()       # Inherited from A
obj_b.print_method()  # Defined in B
obj_b.show()          # Overridden in B
print()

# Object of Subclass C
obj_c = C()
obj_c.display()  # Inherited from A
obj_c.print_method()  # Inherited from B
obj_c.show()     # Overridden in C
