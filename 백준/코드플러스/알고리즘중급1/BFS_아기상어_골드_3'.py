# https://www.acmicpc.net/problem/16236
from collections import deque
queue = deque()

N = int(input())

maps = [list(map(int, input().split())) for _ in range(0, N)]
visited = [N * [0] for _ in range(0, N)]
size = 2
def bfs(start):
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        # visited[y][x] = 1
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = i+x, j+y
            if 0<=nx<N and 0<=ny<N and visited[ny][nx]==0 and maps[ny][nx] !=0:
                if maps[ny][nx] < size:
                    visited[ny][nx] = visited[y][x] + 1
                    # size + 1
                elif maps[ny][nx] == size:
                    visited[ny][nx] = visited[y][x] + 1

for i in range(0, N):
    for j in range(0, N):
        if maps[j][i] == 9 and visited[j][i] == 0:
            bfs((i, j))

max_=0
for i in range(0, N):
    for j in range(0, N):
        max_=max(max_, visited[j][i])
print(max_)