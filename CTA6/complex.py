import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        conjugate = Complex(no.real, -no.imaginary)
        denominator = no.real ** 2 + no.imaginary ** 2
        numerator = self * conjugate
        real = numerator.real / denominator
        imaginary = numerator.imaginary / denominator
        return Complex(real, imaginary)

    def mod(self):
        modulus = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(modulus, 0)

    def __str__(self):
        if self.imaginary == 0:
            return "{:.2f}+0.00i".format(self.real)
        elif self.real == 0:
            return "0.00{:+.2f}i".format(self.imaginary)
        else:
            return "{:.2f}{:+.2f}i".format(self.real, self.imaginary)