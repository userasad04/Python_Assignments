# =========================
# Abstract Classes in Python
# =========================
from abc import ABC, abstractmethod

# -------------------------
# Base Abstract Class
# -------------------------
class Polygon(ABC):
    """
    Abstract base class for polygons.
    Requires subclasses to implement noofsides() method.
    """
    @abstractmethod
    def noofsides(self):
        pass


# -------------------------
# Subclasses implementing abstract method
# -------------------------
class Triangle(Polygon):
    def noofsides(self):
        print("Triangle: I have 3 sides")


class Quadrilateral(Polygon):
    def noofsides(self):
        print("Quadrilateral: I have 4 sides")


class Pentagon(Polygon):
    def noofsides(self):
        print("Pentagon: I have 5 sides")


class Hexagon(Polygon):
    def noofsides(self):
        print("Hexagon: I have 6 sides")


# -------------------------
# Driver Code
# -------------------------
shapes = [Triangle(), Quadrilateral(), Pentagon(), Hexagon()]

for shape in shapes:
    shape.noofsides()
