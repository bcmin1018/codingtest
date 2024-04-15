from collections import deque

M,N,K = map(int, input().split())
maps = [[0] * N for _ in range(0, M)]
visited = [[0] * N for _ in range(0, M)]

# 직사각형 그리기
for _ in range(0, K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if maps[y][x] == 0:
                maps[y][x] = 1

def bfs(node):
    x, y = node[0], node[1]
    queue = deque([])
    queue.append([x, y])
    visited[y][x] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+i, y+j
            if 0<=nx<N and 0<=ny<M and visited[ny][nx] == 0 and maps[ny][nx] == 0:
                visited[ny][nx] = 1
                cnt += 1
                queue.append([nx, ny])
    return cnt


answer = []
for y_ in range(0, M):
    for x_ in range(0, N):
        if visited[y_][x_] == 0 and maps[y_][x_] == 0:
            cnt = bfs([x_, y_])
            answer.append(cnt)
print(len(answer))
n_answer = sorted(answer)
print(' '.join(map(str, n_answer)))










