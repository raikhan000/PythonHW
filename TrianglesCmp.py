from math import sqrt
class Triangle:
    x = 0.0
    y = 0.0
    z = 0.0
    empty = False

    def __init__(self, _x, _y, _z):
        self.x = float(_x)
        self.y = float(_y)
        self.z = float(_z)
        if (_z >= _x + _y or _x >= _z + _y or _y >= _x + _z) or (
                _x < 0 or _y < 0 or _z < 0):
            self.empty = True
    def __abs__(self):
        if self.empty:
            return 0.0
        else:
            p = (self.x + self.y + self.z) / 2
            return sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))
    def __bool__(self):
        return not self.empty
    def __eq__(self, other):
        a = (self.x, self.y, self.z)
        b = (other.x, other.y, other.z)
        return sorted(a) == sorted(b)
    def __le__(self,other):
        return abs(self) == abs(other)
    def __ge__(self, other):
        return abs(self) >= abs(other)
    def __ne__(self,other):
        return abs(self) != abs(other)
    def __gt__(self, other):
        return abs(self) > abs(other)
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __str__(self):
        return f"{self.x}:{self.y}:{self.z}"