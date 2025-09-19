# =========================
# Access Modifiers in Python
# =========================

# -------------------------
# Superclass
# -------------------------
class Super:
    # Public data member
    var1 = None
    # Protected data member
    _var2 = None
    # Private data member
    __var3 = None

    # Constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # Public method
    def displayPublicMembers(self):
        print("Public Data Member:", self.var1)

    # Protected method
    def _displayProtectedMembers(self):
        print("Protected Data Member:", self._var2)

    # Private method
    def __displayPrivateMembers(self):
        print("Private Data Member:", self.__var3)

    # Public method to access private method
    def accessPrivateMembers(self):
        self.__displayPrivateMembers()


# -------------------------
# Derived Class
# -------------------------
class Sub(Super):
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    # Public method to access protected method from superclass
    def accessProtectedMembers(self):
        self._displayProtectedMembers()


# -------------------------
# Driver Code
# -------------------------
obj = Sub("Syed Asad", 5, "CSE")

# Access public method
obj.displayPublicMembers()

# Access protected method via public method
obj.accessProtectedMembers()

# Access private method via public method
obj.accessPrivateMembers()

# Direct access to protected member (possible but not recommended)
print("Direct access to protected member:", obj._var2)

# Direct access to private member (will raise AttributeError if uncommented)
# print(obj.__var3)
