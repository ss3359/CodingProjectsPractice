from complex import Complex


class Riemann:
    def __init__(self, r,c):
        self.number = Complex(r,c)
    def zeta_function(self):
        '''
        Riemann Zeta Function
        ζ(s) = sum_n=1^infty 1/n^s
        
        Complex Exponents
        n^s = n^(a+bi) = (n^a)(n^bi) = (n^a)(exp(ln(bi))) = (n^a)()
        '''

        s = self.number
        sum=0
        term_2= Complex.Exp(Complex.Log(s))
        for n in range(5):
            real = n**s.real 

        



    


def main(): 
    pass

if __name__=="__main__": 
    main()