# https://www.acmicpc.net/problem/1260
# https://www.youtube.com/watch?v=kkZFEwoZ3fA&list=PLodgw23vNd_VTBKHg-WgxQSD_wTPgtyzN&index=1
import sys
# sys.stdin = open("input.txt", "r")

def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1          # 방문 표시

    for n in adj[c]:
        if not v[n]:
            dfs(n)

N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 시작 노드
adj = [[]for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 오르차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N + 1)
ans_dfs = []
dfs(V)

v = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(ans_dfs)
print(ans_bfs)