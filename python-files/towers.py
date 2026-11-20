def print_move(n: int, f: int ,t: int): 
    print(f"Move Disk: {n} from stack {f} to stack {t}")

def towers_of_hanoi(n: int, f: int, t: int, s: int): 

    if(n==1):
        print_move(n,f,t)
        return 
    towers_of_hanoi(n-1,f,s,t)
    print_move(n,f,s)
    towers_of_hanoi(n-1,s,t,f)

def main(): 
    tower_1 = 1    
    tower_2=  2 
    tower_3 = 3
    n_discs = 4 

    towers_of_hanoi(n_discs,tower_1,tower_2,tower_3)

if __name__ =="__main__": 
    main()
