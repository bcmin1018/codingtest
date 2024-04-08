from collections import deque
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

Y, X = map(int, input().split())

maps = []
for _ in range(0, Y):
    maps.append(list(map(int, input().split())))

visited = [[0] * X for _ in range(0, Y)]

def bfs(node):
    x, y = node[0], node[1]
    visited[y][x] = 1
    queue = deque([node])
    cnt=1
    while queue:
        x, y = queue.popleft()
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x+i, y+j
            if 0<=nx<X and 0<=ny<Y and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = 1
                queue.append((nx, ny))
                cnt+=1
    return cnt


answer = []
for y_ in range(0, Y):
    for x_ in range(0, X):
        if visited[y_][x_] == 0 and maps[y_][x_] == 1:
            answer.append(bfs((x_, y_)))

print(len(answer))
if len(answer) > 0:
    print(max(answer))
else:
    print(0)




