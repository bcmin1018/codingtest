# https://www.acmicpc.net/problem/1012
from collections import deque
# recursionerror 발생으로 추가
import sys
sys.setrecursionlimit(10**5)


T = int(input())
for i in range(0, T):
    M, N, K = map(int, input().split())
    #M 가로길이, N 세로길이
    bat = list([0] * (M+2) for _ in range(N+2))
    visited = list([0] * (M+2) for _ in range(N+2))

    for _ in range(0, K):
        i, j = map(int, input().split()) #i 가로길이 j 세로길이
        bat[j+1][i+1] = 1

    # dfs 구현
    # def dfs(i, j):
    #     #탐색을 한 곳은 1로 표시
    #     visited[j][i] = 1
    #     for p, q in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
    #         ni, nj = i+p, j+q
    #         # 방문 했거나 배추가 없으면 스킵
    #         if visited[nj][ni] == 1 or bat[nj][ni] == 0:
    #             continue
    #         dfs(ni, nj)
    #

    # bfs 구현
    def bfs(i, j):
        visited[j][i] = 1
        queue = deque()
        queue.append([i, j])
        while queue:
            node = queue.popleft()
            for p, q in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = node[0]+p, node[1]+q
                if visited[nj][ni] == 1 or bat[nj][ni] == 0:
                    continue
                bfs(ni, nj)

    ans = 0
    # 전체 밭을 돌아다니면서 방문을 안하고 배추가 있으면 DFS 탐색 시작
    for j in range(N+1):
        for i in range(M+1):
            if visited[j][i] == 0 and bat[j][i] == 1:
                # 배추가 있는 곳에서 탐색 시작
                # dfs(i, j)
                bfs(i, j)
                # 탐색이 끝났으면 +1
                ans += 1
    print(ans)







