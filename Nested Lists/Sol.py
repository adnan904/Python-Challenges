def main():
    # Create an Empty Dictionary
    dict = {}
    n = int(input())
    # Adding Key-Value pairs to the dictionary
    for _ in range(n):
        name = input()
        score = float(input())
        dict[name] = score
    # Extracting only the Grades from the dictionary
    keys = list(dict.values())
    # Sorting them in Descending order
    keys.sort(reverse=True)
    # Finding the Second last Grade
    i = n - 2

    '''
    # Consider the following test cases as well: 
    1) A:10, B:9 , C:8, D:6, E:6, f:5 , G:5
    2) A:-2, B:-3 , C:-4, D:-5, E:-5, f:-6 , G:-6 
    '''
    while (keys[i] == keys[n - 1] and i>=0):
        i = i - 1
    second = keys[i]

    #Extracting names of all students that have the second lowest grade
    names = []
    for name, grade in dict.items():
        if grade == second:
            names.append(name)
    #Sorting names in the ascending order if more than one student has the 2nd lowest grade
    names.sort()
    for name in names:
        print(name)

if __name__ == "__main__":
    # execute only if run as a script
    main()
