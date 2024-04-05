#https://www.acmicpc.net/problem/4963

import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = []
    for _ in range(0, h):
        maps.append(list(map(int, input().split())))

    visited = [[0] * w for _ in range(0, h)]
    answer = 0
    def dfs(node):
        w_, h_ = node
        visited[h_][w_] = 1
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x+w_, y+h_
            if 0<=nx<w and 0<=ny<h and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dfs((nx, ny))

    for h_ in range(0, h):
        for w_ in range(0, w):
            if visited[h_][w_] == 0 and maps[h_][w_] == 1:
                dfs((w_, h_))
                answer += 1

    print(answer)

