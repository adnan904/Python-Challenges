def str_format(n):
    width =len("{0:b}".format(n))
    output=[]
    for i in range(1,n+1):
        output.append("{:>{wide}}".format(i,wide=width)
                      + " " +
                      "{:>{wide}}".format(oct(i)[2:],wide=width)
                      + " " +
                      "{:>{wide}}".format((hex(i)[2:]).upper(),wide=width)
                      + " " +
                      "{:>{wide}}".format(bin(i)[2:],wide=width)
                      )
    output = "\n".join(output)
    print(output)

if __name__== "__main__":
    n = int(input())
    str_format(n)
