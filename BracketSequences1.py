import math
import sys

base = int(1e9 + 7)
my_dict = {}


def solve(x, y):
    key = str(x) + "-" + str(y)
    if key in my_dict:
        return my_dict[key]

    if (x, y) == (0, 0):
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x

    res = 0
    if x - 1 >= y and x - 1 >= 0:
        res += (solve(x - 1, y) % base)
    if 0 <= y - 1 <= x:
        res += (solve(x, y - 1) % base)

    my_dict[key] = res % base
    return res


def solve2(n2):
    # n2 is assumed even
    n = n2 // 2
    dp = [[0]]
    for i in range(1, n + 1):
        dp.append([])
        for j in range(0, i + 1):
            dp[i].append(0)
            if j == 0:
                dp[i][j] = 1
                continue
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % base
            if i - 1 >= j:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % base
    return dp[n][n]


num = int(input().strip())
if num % 2 == 1:
    print(0)
    sys.exit()

# Catalan Number
half = num // 2
print((math.comb(num, half) // (half + 1)) % base)
