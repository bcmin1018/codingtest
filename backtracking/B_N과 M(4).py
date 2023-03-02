# https://www.acmicpc.net/problem/15652
# https://www.youtube.com/watch?v=JqU56H0OIaY&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=6

import sys
sys.stdin = open("input.txt", "r")

def dfs(n, s, lst):
    if n == N:
        ans.append(lst)
        return
    for c in range(s, M+1):
        dfs(n+1, c, lst+[c])

M, N = map(int, input().split())
ans = []
dfs(0, 1, [])
for lst in ans:
    print(*lst)