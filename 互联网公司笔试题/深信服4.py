def getComm(s1, s2):
    m = min(len(s1), len(s2))
    for i in range(m+1):
        if i >= m:
            return m
        if s1[i] != s2[i] and i < m:
            return i

def getRe(s):
    arr = []
    for i in range(len(s)):
        arr.append([s[i:], i])
    arr.sort(key=lambda i:i[0])
    max_len = 0
    start, end = 0, 0
    for i in range(len(s)-1):
        curr_len = getComm(arr[i][0], arr[i+1][0])
        if max_len < curr_len:
            max_len = curr_len
            start = arr[i][1]
            end = arr[i+1][1]
    min_idx = min(start, end)
    max_idx = max(start, end)
    middle = min_idx + max_len - max_idx
    return 2*max_len - middle


if __name__ == "__main__":
    s = input()
    print(getRe(s))