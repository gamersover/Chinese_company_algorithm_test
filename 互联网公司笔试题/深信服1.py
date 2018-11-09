def catch(n, k, number):
    if n == 1:
        return "YES"
    elif n == 2 and k == 1:
        return "NO"
    elif n == 2 and k >= 2:
        if "11" in number or "22" in number:
            return "YES"
        else:
            return "NO"
    elif n == 3:
        if "22" in number:
            return "YES"
        else:
            return "NO"
    elif n == 4:
        if "223" in number:
            return "YES"
        else:
            return "NO"
    return "NO"

if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]
    number = ''.join(input().split())
    print(catch(n, k, number))