import numpy 

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
        '''
        (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        '''
        result = Complex(0.0, 0.0)
        result.real=(self.real*other.real)-(self.imag*other.imag)
        result.imag=(self.real+other.imag)+(self.imag*other.real)
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
        '''(a+bi)/(c+di) = (a+bi)*(c-di)/(c*c + d*d)'''
        pass
def print_complex_number(c : Complex):
    print(f"{c.real} + {c.imag}i")

def main(): 
    v1 = Complex(1.2, 4.3)
    v2 = Complex(1.3,4.5)
if __name__ == "__main__":
    main() 
