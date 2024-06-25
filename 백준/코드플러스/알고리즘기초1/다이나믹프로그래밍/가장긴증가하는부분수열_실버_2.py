# https://www.acmicpc.net/problem/11053
N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    mx = 0
    for j in range(0, i): # 이전까지의 숫자를 모두 순회 하면서 현재보다 큰게 있는지 확인한다.
        if lst[i] > lst[j]:
            mx = max(mx, dp[j]) #
    dp[i] = mx + 1 # 이전까지 숫자 중에서 가장 큰 값보다 + 1

print(max(dp))
