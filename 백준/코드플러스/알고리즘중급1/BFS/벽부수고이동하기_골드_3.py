# https://hongcoding.tistory.com/18
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
v = [[[0] * 2 for _ in range(M)] for _ in range(N)]
def bfs(x, y):

    q = deque()
    q.append((x, y, 0))
    v[y][x][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == M - 1 and y == N - 1:
            return v[N-1][M-1][z]

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= ny < N:
                if maps[ny][nx] == 1 and z == 0:
                    v[ny][nx][1] = v[y][x][0] + 1
                    q.append((nx, ny, 1))
                if maps[ny][nx] == 0 and v[ny][nx][z] == 0:
                    v[ny][nx][z] = v[y][x][z] + 1
                    q.append((nx, ny, z))

    return -1

print(bfs(0, 0))
