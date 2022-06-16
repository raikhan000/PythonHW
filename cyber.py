from math import floor
from fractions import Fraction

class Sausage:
    __meat = ""
    __vol = 0
    def __init__(self, meat = "pork!", vol = 1):
        self.__meat = meat
        if Fraction(vol) >= 0:
            self.__vol = Fraction(vol)*12

        else:
            self.__vol = Fraction(0)
    def construct_sausage(self, n, c):
        len_of_meat = n % len(self.__meat)
        start = "/" + ("-" * n) + c
        filling = "|" + (self.__meat * (floor(n / len(self.__meat))))
        filling += (self.__meat[:len_of_meat]) + "|"
        if c == '\\':
            end = "\\" + ("-" * n) + "/"
        else:
            end = "\\" + ("-" * n) + "|"
        return start, filling, end

    def __str__(self):
        start = ""
        end = ""
        filling = ""
        len_of_sausage = self.__vol
        while len_of_sausage >= 12:
            s, f, e = self.construct_sausage(12, "\\")
            start += s
            filling += f
            end += e
            len_of_sausage -= 12
        if 0 < len_of_sausage < 12 or self.__vol == 0:
            s, f, e = self.construct_sausage(int(len_of_sausage), "|")
            start += s
            filling += f
            end += e
        return start + "\n" + (filling + "\n") * 3 + end

    def __bool__(self):
        return bool(self.__vol)
    
    def __add__(self, other):
        return Sausage(self.__meat, (self.__vol + other.__vol) / 12)

    def __sub__(self, other):
        return Sausage(self.__meat, (self.__vol - other.__vol) / 12)

    def __mul__(self, other):
        return Sausage(self.__meat, (self.__vol * other) / 12)

    def __rmul__(self, other):
        return Sausage(self.__meat, (self.__vol * other) / 12)

    def __abs__(self):
        return f'{self.__vol / 12}'

    def __truediv__(self, other):
        return Sausage(self.__meat, (self.__vol / other) / 12)

