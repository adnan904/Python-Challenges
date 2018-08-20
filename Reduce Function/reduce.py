from fractions import Fraction
from functools import reduce

def product(fracs):
    #fracs is a list having instances of Fraction type , eg: fracs = [Fraction(1,2),Fraction(3,4)......]
    #Applying arithematic operations like add,mul,sub etc on Fraction objects is possible
    #(lambda arguments: manipulation), lambda function takes two of instances from fracs as arguments(provided from source by reduce) and multiply them
        #reduce(operation,source) , source is an iterable list. reduce selects the first two items of the iterable, performs the operation on them
        #next the result and the 3rd item are used for the operation and so on until the opration results in a single item
    t=reduce(lambda frac1,frac2 : frac1*frac2,fracs)  # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        #Since each line in the input has 2 numbers, we split then and use the map to cast them to int
        #map(func,iterable), map applies the 1st argument which is a function on each item in the iterable
        #input.split() in this case will be a list having 2 numbers
        num,den=map(int,input().split())
        #the return type will be an instance of the Fraction class e.g: Fraction(8,9)
        frac = Fraction(num,den)
        fracs.append(frac)
        #fracs.append(Fraction(*map(int, input().split())))
    print(fracs)
    result = product(fracs)
    print(*result)