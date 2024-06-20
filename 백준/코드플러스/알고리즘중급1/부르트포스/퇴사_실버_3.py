# https://www.acmicpc.net/problem/14501
# 1일부터 7일 까지 순회하며 최적의 답을 그냥 잔인하게 찾아보자
# 주의 할 점은 상담 비용이 최우선이 아니라 상담 개수가 최우선이다.

# DFS 풀이
N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

def dfs(n, sum_):
    global ans
    if n >= N:
        ans = max(ans, sum_)
        return

    if n + T[n] <= N: # 퇴사일 범위 내에 있는 경우 상담 시작
        dfs(n+T[n], sum_+P[n])

    # 상담 안하는 경우
    dfs(n+1, sum_)

ans = 0
dfs(0, 0)

print(ans)


# DP
