# https://www.youtube.com/watch?v=N_4tI8xvhR4&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=4

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm, v):
    global ans
    if n == N:
        ans = min(ans, sm)
        return

    if ans <= sm:
        return

    for j in range(0, N):
        if j not in v:
            dfs(n+1, sm + lst[j][n], v+[j])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(0, N)]
    # v = [0] * N
    ans = 100 * N
    dfs(0, 0, [])
    print(f'#{test_case} {ans}')