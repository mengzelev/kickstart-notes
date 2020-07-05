def solve(N: int)->int:
    s, high = '0' + str(N), 0
    up, low = N, N
    for i, c in enumerate(s):
        if int(c) & 1:
            # Find the largest even-digited number smaller than N
            if i + 1 == len(s):
                low = int(str(int(s[0:i+1])-1))
            else:
                low = int(str(int(s[0:i+1])-1) + ('8' * (len(s)-i-1)))
            # Find the smallest even-digited number larger than N
            if c == '9':
                j = i - 1
                while j > 0 and s[j] == '8': j -= 1
                up = (int(s[0:j+1])+2) * (10 ** (len(s)-j-1))
            else:
                up = (int(s[0:i+1])+1) * (10 ** (len(s)-i-1))
            break
    # print('up=%d, low=%d' % (up, low))
    return min(up-N, N-low)


if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        N = int(input().strip())
        print('Case #%d: %d' % (i+1, solve(N)))