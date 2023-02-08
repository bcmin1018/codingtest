# https://www.acmicpc.net/problem/2644
# https://www.youtube.com/watch?v=j1qZDHllov8&list=PLodgw23vNd_VTBKHg-WgxQSD_wTPgtyzN&index=5
# 이 문제의 경우 깊이를 촌수로 계산하면 되기 때문에 BFS가 맞다.

import sys
sys.stdin = open("input.txt", "r")

def bfs(S, E):
    q = []
    q.append(S)
    visited_bfs[S] = 1

    while q:
        c = q.pop(0)
        if c == E: # 목적지를 찾음
            return visited_bfs[E] -1
        for child in arr[c]:
            if not visited_bfs[child]:
                q.append(child)
                visited_bfs[child] = visited_bfs[c] + 1 # 한칸씩 이동하면 숫자가 1이 증가하게 되는데 이것이 촌수를 의미 한다.
    return -1




N = int(input())
S, E = map(int, input().split())
R = int(input())

arr = [[] for _ in range(0, N+1)]

for _ in range(R):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

visited_bfs = [0] * (N + 1)
ans = bfs(S, E)
print(ans)
