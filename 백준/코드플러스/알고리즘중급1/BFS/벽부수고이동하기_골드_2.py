# https://hongcoding.tistory.com/18
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

walls = []
for y in range(N):
    for x in range(M):
        if maps[y][x] == 1:
            walls.append((x, y))

def bfs(node):
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append(node)
    v[node[1]][node[0]] = 1

    while q:
        x, y = q.popleft()
        if x == M - 1 and y == N - 1:
            return v[N-1][M-1]

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= ny < N and v[ny][nx] == 0 and maps[ny][nx] == 0:
                q.append((nx, ny))
                v[ny][nx] = v[y][x] + 1

answer = []
if len(walls) > 0:
    for w in walls:
        maps[w[1]][w[0]] = 0
        d = bfs((0, 0))
        maps[w[1]][w[0]] = 1
        if d == None:
            continue
        else:
            answer.append(d)
else:
    d = bfs((0, 0))
    answer.append(d)


if len(answer) == 0:
    print(-1)
else:
    print(min(answer))
