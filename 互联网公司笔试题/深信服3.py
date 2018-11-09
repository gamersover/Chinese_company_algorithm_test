def printRe(m, a):
    for i in range(m):
        uid = int(input()) 
        if uid not in a:
            a.append(uid)

    print(len(a[:10]))
    print(*a[:10], sep="\n")


if __name__ == "__main__":
    m = int(input())
    a = []
    printRe(m, a)        