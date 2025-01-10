import sys

_, n = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))

c.sort()
dp = [sys.maxsize] * (n + c[-1])
for i in c:
    dp[i] = 1
for k in range(n):
    for i in c:
        dp[k + i] = min(dp[k + i], dp[k] + 1)
print(dp[n] if dp[n] < sys.maxsize else -1)
