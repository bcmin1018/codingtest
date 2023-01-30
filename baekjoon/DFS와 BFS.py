# https://www.acmicpc.net/problem/1260
# https://www.youtube.com/watch?v=kkZFEwoZ3fA&list=PLodgw23vNd_VTBKHg-WgxQSD_wTPgtyzN&index=1
import sys
# sys.stdin = open("input.txt", "r")

# def dfs(c):
#     ans_dfs.append(c) # 방문 노드 추가
#     v[c] = 1          # 방문 표시
#
#     for n in adj[c]:
#         if not v[n]:
#             dfs(n)
#
# def bfs(s):
#     q = []
#     q.append(s)
#     ans_bfs.append(s)
#     v[s] = 1
#
#     while q:
#         c = q.pop(0)
#         for n in adj[c]:
#             if not v[n]:
#                 q.append(n)
#                 ans_bfs.append(n)
#                 v[n] = 1
#
#
# N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 시작 노드
# adj = [[]for _ in range(N+1)]
# for _ in range(M):
#     s, e = map(int, input().split())
#     adj[s].append(e)
#     adj[e].append(s)
#
# # 오름차순 정렬
# for i in range(1, N+1):
#     adj[i].sort()
#
# v = [0] * (N + 1)
# ans_dfs = []
# dfs(V)
#
# v = [0] * (N + 1)
# ans_bfs = []
# bfs(V)
#
# print(ans_dfs)
# print(ans_bfs)

def dfs(V):
    ans_dfs.append(V)
    visited_dfs[V] = 1
    for c in matrix[V]:
        if not visited_dfs[c]:
            dfs(c)

def bfs(V):
    q = []
    q.append(V)
    ans_bfs.append(V)
    visited_bfs[V] = 1

    while q:
        s = q.pop(0)
        for c in matrix[s]:
            if not visited_bfs[c]:
                q.append(c)
                ans_bfs.append(c)
                visited_bfs[c] = 1



N, M, V = map(int, input().split())

matrix = [[] for _ in range(0, N+1)]
for _ in range(0, M):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

# 정점 안에 있는 순서는 오름차순으로 방문해야하기 때문에 sort 진행
for node in matrix:
    node.sort()

ans_dfs = []
visited_dfs = [0] * (N + 1)
dfs(V)

ans_bfs = []
visited_bfs = [0] * (N + 1)
bfs(V)

print(ans_dfs)
print(ans_bfs)