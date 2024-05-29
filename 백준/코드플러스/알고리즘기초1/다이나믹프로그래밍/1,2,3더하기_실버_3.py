import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(input())
    dp = [0] * (n+4)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])




