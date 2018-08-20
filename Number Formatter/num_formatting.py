import re
def validate(num):
    if(re.match("^[+-]?[0-9]*\.[0-9]+$", num)):
        return True
    return False




if __name__ =='__main__':
    n=int(input())
    numbers=[]
    for _ in range(n):
        numbers.append(input())
    for num in numbers:
        result=validate(num)
        print(result)