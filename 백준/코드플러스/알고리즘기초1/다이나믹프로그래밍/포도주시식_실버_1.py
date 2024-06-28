N = int(input())
w = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
dp[1] = w[1]

if N > 1:
    dp[2] = w[1] + w[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i])
print(max(dp))
