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
    def __pow__(self,other):
        result = Complex(0.0,0.0)
        a = self.real
        b = self.imag 
        c = other.real
        d = other.imag 

        r = np.sqrt(a**2 + b**2)
        theta = np.atan(b/a)
        result.real = (r**c)*(np.exp(-d*theta))*np.cos(c*theta + d*np.ln(r))
        result.imag = (r**c)*(np.exp(-d*theta))*np.sin(c*theta + d*np.ln(r))

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

    @staticmethod
    def polar_form(z:Complex):
        r= np.sqrt((z.real**2) + (z.imag**2))
        theta = np.atan(z.imag/z.real)
        return Complex(r*np.cos(theta),r*np.sin(theta))
    
    @staticmethod
    def Exp(z:Complex): 
        result =Complex(0.0,0.0)
        result.real = np.exp(z.real)*np.cos(z.imag)
        result.imag = np.exp(z.real)*np.sin(z.imag)
        return result
    
    @staticmethod
    def Log(z:Complex):
        result = Complex(0.0,0.0)
        r = z.real**2 + z.imag**2
        theta = np.atan(z.imag/z.real)
        result.real = np.ln(r)
        result.imag=theta
        return result
        
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
