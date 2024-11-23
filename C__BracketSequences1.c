#include <stdio.h>

int main()
{
    printf("Hello World");
    int n2 = 0;
    long long base = 1000000007;
    scanf("%d", &n2);

    if(n2 % 2 == 1) {
        printf("0");
    } else {
        int n = n2 / 2;
        int dp[n+1][n+1];

        int i = 0, j = 0;
        for(i = 1; i <= n; i++) {
            for(j = 0; j <= i; j++) {
                if(j == 1) {
                    dp[i][j] = i;
                    continue;
                }
                dp[i][j] = 0;
                if(j > 0) {
                    dp[i][j] = (dp[i][j] + dp[i][j - 1]) % base;
                }
                if(i-1 >= j) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % base;
                }
            }
        }
        printf("%d", dp[n][n]);
    }
}