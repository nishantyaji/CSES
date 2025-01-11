base = 1000000007
_, n = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))

dp = [0] * (n + 1)
for i in c:
    if i <= n:
        dp[i] = 1
for k in range(n):
    for i in c:
        if k + i <= n:
            dp[k + i] = (dp[k + i] + dp[k]) % base
print(dp[n])

"""
This solution times out in python.
But it does not time out in C

/******************************************************************************

                            Online C Debugger.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Debug" button to debug program.

*******************************************************************************/
#include <stdlib.h>
#include <stdio.h>

int main()
{

    int size = 0, n = 0, i = 0, j = 0, max = 0, base = 1000000007;
    scanf("%d", &size);
    scanf("%d", &n);

    int * c = (int *) malloc(sizeof(int) * size);

    for(i = 0; i < size; i++) {
        scanf("%d", &c[i]);
        max = max > c[i] ? max : c[i];
    }
    int * dp = (int *) malloc(sizeof(int) * (n + 1));
    for( i = 0; i < n + 1; i++) {
        dp[i] = 0;
    }
    for(i = 0; i < size; i++) {
        if(c[i] <= n) {
            dp[c[i]] = 1;
        }
    }
    for(i = 0; i < n; i++){
        for(j = 0; j < size; j++) {
            if(i + c[j] <= n) {
                dp[i + c[j]] = (dp[i + c[j]] + dp[i]) % base;
            }
        }
    }
    printf("%d", dp[n]);
}
"""
