# https://www.acmicpc.net/problem/11053
N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N):
    if lst[i] < lst[i+1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(max(dp)+1)
