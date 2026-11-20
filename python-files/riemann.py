from complex import Complex, print_complex_number


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
        sum=Complex(0.0,0.0)
        print(f"Initial Sum S = {sum}")
        for n in range(1,100,1):
            n_complex = Complex(n,0.0)
            sum+=Complex(1.0,0.0)/(n_complex**s)
            print(f"Sum at n = {n}")
            print_complex_number(sum)
            print()

        



    


def main(): 
    s = Riemann(1.0,1.0)
    s.zeta_function()
    

if __name__=="__main__": 
    main()