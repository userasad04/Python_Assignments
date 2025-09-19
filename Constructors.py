# =========================
# Constructors in Python
# =========================

# -------------------------
# Example 1: Default Constructor
# -------------------------
class A:
    def __init__(self):  # default constructor
        self.name = "Syed Asad"
    
    def print_A(self):
        print("Name from class A:", self.name)

obj_a = A()
obj_a.print_A()


# -------------------------
# Example 2: Constructor in Inherited Class
# -------------------------
class B(A):
    def __init__(self):  # constructor overrides parent
        self.name = "Syed Asad"
    
    def print_B(self):
        print("Name from class B:", self.name)

obj_b = B()
obj_b.print_B()


# -------------------------
# Example 3: Public, Protected, and Private Members
# -------------------------
class C:
    name = None
    _roll = None
    __branch = None

    def __init__(self, name, roll, branch):
        self.name = name
        self._roll = roll
        self.__branch = branch

    def displayName(self):
        print("Name:", self.name)

    def _displayRoll(self):
        print("Roll:", self._roll)

    def __displayBranch(self):
        print("Branch:", self.__branch)

    def access__displayBranch(self):
        self.__displayBranch()


# -------------------------
# Example 4: Accessing Parent Members in Derived Class
# -------------------------
class D(C):
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)

    def access_displayRoll(self):
        self._displayRoll()


# Creating object of derived class D with your name
obj_d = D("Syed Asad", 5, "CSE")

obj_d.displayName()
obj_d.access_displayRoll()
obj_d.access__displayBranch()
