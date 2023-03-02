# youtube.com/watch?v=aofZJvWjZIY&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=5
# https://www.acmicpc.net/problem/15651

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for c in range(1, N+1):
        dfs(n+1, lst + [c])

N, M = map(int, input().split())
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)
