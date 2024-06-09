# https://www.acmicpc.net/problem/11052

N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j - i >= 9:
            dp[j] = max(dp[j], dp[j - i] + lst[i])
        print(dp[N])