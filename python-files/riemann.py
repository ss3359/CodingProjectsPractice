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
        print(f"Initial Sum S = {sum}")
        for n in range(5):
            sum+=n**s
            print("Sum at n = {n} => S = {sum}")

        



    


def main(): 
    pass

if __name__=="__main__": 
    main()