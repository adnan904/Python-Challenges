def main():
    dict = {}
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        dict[name] = score
    #print(dict)
    keys = list(dict.values())
    keys.sort(reverse=True)
    #print(keys)
    i = n - 2
    while (keys[i] <= keys[n - 1] and i>=0):
        i = i - 1
    second = keys[i]

    for name,grade in dict.items():
        if grade==second:
            print(name)


if __name__ == "__main__":
    # execute only if run as a script
    main()
