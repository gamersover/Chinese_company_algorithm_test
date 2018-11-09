def getRe(s, n):
    end = 2**n - 1
    while end > 0:
        arr = [int(i) for i in bin(end)[2:]]
        arr = [0]*(n-len(arr)) + arr
        re = sum(map(lambda i, j:i*j, arr, s))
        if re == 100:
            return arr
        end -= 1
    
    
if __name__ == "__main__":
    n = int(input())
    scores = [int(input()) for i in range(n)]
    arr = getRe(scores, n)
    print(sum(arr))
    for i in range(n):
        if arr[i] == 1:
            print(i+1)
