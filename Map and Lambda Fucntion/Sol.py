#  Lambda is a single expression anonymous function often used as an inline function. In #  simple words, it is a function that has only one line in its body. 

cube = lambda x: x**3 # computes the cube of x 

def fibonacci(n):
    # returns a list of first 'n' fibonacci numbers
    fib=[]
    first=0
    second=1
    fib.append(first)
    fib.append(second)
    index=3
    while(index<=n):
        sum=first+second
        fib.append(sum)
        first=second
        second=sum
        index+=1
    return(fib)

if __name__ == "__main__":
    n=int(input())
	'''
		The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables. 
		In this case it will apply the lambda function "cube" to each number in fibonacci list
	'''
	print(list(map(cube, fibonacci(n))))
