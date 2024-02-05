import math
class Complex: 
    def __init__(self, R,I):
        self.Real,self.Imaginary= R, I

    def __str__(self):
        return f"{self.Real} + {self.Imaginary}i"

    def Magnitude(self):
        return math.sqrt(self.Real**2 + self.Imaginary**2)

    def Orientation(self):
        return math.atan(self.Imaginary/self.Real)


num1 = Complex(3,4)
print(num1.__str__())
print(num1.Magnitude())
print(num1.Orientation())