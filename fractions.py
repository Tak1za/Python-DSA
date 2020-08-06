class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherFraction):
        newNum = self.num*otherFraction.den + self.den*otherFraction.num
        newDen = self.den*otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum == secondNum

    def __mul__(self, other):
        newNum = self.num * other.num
        newDen = self.den * other.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __sub__(self, other):
      newNum = self.num * other.den - self.den * other.num
      newDen = self.den * other.den
      common = gcd(newNum, newDen)
      return Fraction(newNum//common, newDen//common)

    def __div__(self, other):
      newNum = self.num * other.den
      newDen = self.den * other.num
      common = gcd(newNum, newDen)
      return Fraction(newNum, newDen)


def gcd(m, n):
    while m % n != 0:
        oldM = m
        oldN = n

        m = oldN
        n = oldM % oldN
    return n


myFraction = Fraction(3, 5)
print(myFraction)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1+f2)
print(f1 == f2)
print(f1 * f2)
print(f1 - f2)
print(f1 / f2)