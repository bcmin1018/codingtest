N, M = map(int, input().split())

maps = []
for _ in range(0, M):
    maps.append(list(input()))

visited = [[0] * N for _ in range(0, M)]

cnt = 0
def dfs(node, flag, cnt):
    x, y = node[0], node[1]
    visited[y][x] = 1
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+i, y+j
        if 0<= nx < N and 0<= ny < M and visited[ny][nx] == 0 and maps[ny][nx] == flag:
            visited[ny][nx] = 1
            cnt = dfs((nx, ny), flag, cnt+1)
    return cnt

answer = [0, 0]
for m in range(0, M):
    for n in range(0, N):
        if maps[m][n] == "W" and visited[m][n] == 0:
            w_cnt = dfs((n, m), "W", 1)
            answer[0] += w_cnt**2
        if maps[m][n] == "B" and visited[m][n] == 0:
            b_cnt = dfs((n, m), "B", 1)
            answer[1] += b_cnt**2
print(f'{answer[0]} {answer[1]}')