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

"""
This times out in python
But succeeds in C

----------------------------------------------------------------------
#include <stdlib.h>
#include <stdio.h>

int main()
{

    int size = 0, n = 0, i = 0, j = 0, max = 0, limit = 2147483646;
    scanf("%d", &size);
    scanf("%d", &n);

    int * c = (int *) malloc(sizeof(int) * size);

    for(i = 0; i < size; i++) {
        scanf("%d", &c[i]);
        max = max > c[i] ? max : c[i];
    }
    int * dp = (int *) malloc(sizeof(int) * (n + max + 2));
    for( i = 0; i < n + max + 1; i++) {
        dp[i] = limit;
    }
    for(i = 0; i < size; i++) {
        dp[c[i]] = 1;
    }
    for(i = 0; i < n; i++){
        for(j = 0; j < size; j++) {
            dp[i + c[j]] = (dp[i+c[j]]) < (dp[i] + 1) ? dp[i+c[j]] : (dp[i] + 1);
        }
    }
    printf("%d", dp[n] == limit? -1 : dp[n]);
}
-----------------------------------------------------------------
"""