# https://www.acmicpc.net/problem/2606
# https://www.youtube.com/watch?v=QBw5NzoRogg&list=PLodgw23vNd_VTBKHg-WgxQSD_wTPgtyzN&index=3

import sys
sys.stdin = open("input.txt", "r")

def dfs(c):
    global ans
    ans += 1
    v[c] = 1
    for child in arr[c]:
        if not v[child]:
            dfs(child)


C = int(input())
N = int(input())
arr = [[] for _ in range(C+1)]

for i in range(N):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

ans = 0
v = [0] * (C+1)
dfs(1)
print(ans -1)
