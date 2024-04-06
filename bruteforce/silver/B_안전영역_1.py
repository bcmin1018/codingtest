# dfs로 푼 경우 재귀 리밋에 걸려 bfs로 변환하여 성공

N = int(input())
maps = [list(map(int, input().split())) for _ in range(0, N)]

max_ = 0
for map in maps:
    if max_ < max(map):
        max_=max(map)

# def dfs(node):
#     x, y = node[0], node[1]
#     visited[y][x] = 1
#     for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#         nx, ny = x+i, y+j
#         if 0<=nx<N and 0<=ny<N and visited[ny][nx] == 0 and maps[ny][nx] > limit:
#             visited[ny][nx] = 1
#             dfs((nx, ny))

from collections import deque

def bfs(node):
    x, y = node[0], node[1]
    visited[y][x] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 and maps[ny][nx] > limit:
                visited[ny][nx] = 1
                queue.append((nx, ny))


result = []
for limit in range(0, max_+1):
    answer = 0
    visited = [[0] * (N) for _ in range(0, N)]
    for i in range(0, N):
        for j in range(0, N):
            if visited[j][i] == 0 and maps[j][i] > limit:
                # dfs((i, j))
                bfs((i, j))
                answer += 1
    result.append(answer)

print(max(result))
