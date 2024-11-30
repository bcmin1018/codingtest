from collections import deque

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(0, N)]
visited = [[0] * M for _ in range(0, N)]
queue = deque()

def bfs(start):
    queue.append(start)
    x, y = start[0], start[1]
    visited[y][x] = 1

    while queue:
        x, y = queue.popleft()
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= ny < N and map[ny][nx] != 0 and visited[ny][nx] == 0:
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
    return visited[N-1][M-1]

print(bfs((0, 0)))