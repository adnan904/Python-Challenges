def get_pattern(n,m):
    pattern = []
    #Creating a list of the upper part, above the Welcome line
    for i in range(n// 2):
        pattern.append(((2 * i + 1) * ".|.").center(m, '-'))
    #reversing the Upper Part as a list
    temp = pattern[::-1]
    pattern.append("WELCOME".center(m, '-'))
    #we cant straight away append temp, as the whole of it will be appended as a single element
    for line in temp:
       pattern.append(line)
    return pattern

if __name__ == "__main__":
    n,m =map(int,input().split())
    result=get_pattern(n,m)
    #result so far is a list having indivual elements as lines that we need to print
    #So we can either use a for loop to print those lines or we join them as a single string
    result='\n'.join(result)
    print(result)
