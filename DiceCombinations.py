base = 1000000007
n = int(input().strip())

dp = [0] * (n + 6)
for i in range(1, 7):
    dp[i] = 1
for k in range(n):
    for i in range(1, 7):
        dp[k + i] = (dp[k + i] + dp[k]) % base
print(dp[n])
