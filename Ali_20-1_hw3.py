class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def GCD(self, a, b):
        return self.GCD(b, a % b) if b else a

    def __add__(self, other):
        znum = self.denominator * other.denominator // self.GCD(self.denominator, other.denominator)
        chisl = znum // self.denominator * self.numerator + znum // other.denominator * other.numerator
        self.numerator = chisl
        self.denominator = znum
        return Fraction(numerator=chisl, denominator=znum)

    def __sub__(self, other):
        znum = self.denominator * other.denominator // self.GCD(self.denominator, other.denominator)
        chisl = znum // self.denominator * self.numerator - znum // other.denominator * other.numerator
        self.numerator = chisl
        self.denominator = znum
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def __mul__(self, other):
        chisl = self.numerator * other.numerator
        znum = self.denominator * other.denominator
        z = self.GCD(chisl, znum)
        chisl //= z
        znum //= z
        self.numerator = chisl
        self.denominator = znum
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def __floordiv__(self, other):
        x = other.numerator
        other.numerator = other.denominator
        other.denominator = x
        chisl = self.numerator * other.numerator
        znum = self.denominator * other.denominator
        z = self.GCD(chisl, znum)
        chisl //= z
        znum //= z
        self.numerator = chisl
        self.denominator = znum
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


num1 = input("Введите дробь в формате ?/?: ")
num2 = input("Введите дробь в формате ?/?: ")

num1 = num1.split('/')
num2 = num2.split('/')

a = Fraction(int(num1[0]), int(num1[1]))
b = Fraction(int(num2[0]), int(num2[1]))

print(f"{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {a + b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} - {num2[0]}/{num2[1]} = {a - b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {a * b}")
a = Fraction(int(num1[0]), int(num1[1]))
print(f"{num1[0]}/{num1[1]} // {num2[0]}/{num2[1]} = {a // b}")
