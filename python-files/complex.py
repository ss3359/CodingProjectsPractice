import numpy as np 

class Complex: 
    def __init__(self, real,imag):
        self.real=real
        self.imag=imag 

    def __add__(self, other):
        result = Complex(0.0, 0.0)
        result.real=self.real+other.real
        result.imag=self.imag+other.imag
        return result 
    def __mul__(self, other):
        result = Complex(0.0, 0.0)
        result.real=(self.real*other.real)-(self.imag*other.imag)
        result.imag=(self.real*other.imag)+(self.imag*other.real)
        return result 
        
    def __sub__(self, other):
        result = Complex(0.0, 0.0)
        result.real=self.real-other.real
        result.imag=self.imag-other.imag
        return result 
    
    def __truediv__(self, other):
        result = Complex(0.0,0.0)
        length = other.real*other.real+other.imag*other.imag

        result.real = (self.real*other.real + self.imag*other.imag)/length
        result.imag = (-self.real*other.imag + self.imag*other.real)/length

        return result
    
    def polar_form(self):

        r= np.sqrt((self.real**2) + (self.imag**2))
        theta = np.atan(self.imag/self.real)

        return Complex(r*np.cos(theta),r*np.sin(theta))
def print_complex_number(c : Complex):
    print(f"{c.real} + {c.imag}i")

def main(): 
    v1 = Complex(1.0,1.0)
    v1_polar = v1.polar_form()
    print("Cartesian: ")
    print_complex_number(v1)
    print("Polar: ")
    print_complex_number(v1_polar)

if __name__ == "__main__":
    main() 
