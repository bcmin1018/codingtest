import sys

n = int(sys.stdin.readline())
dp = [0] * (n+2)
dp[1], dp[2] = 1, 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

ans = dp[n]
print(ans%10007)