N = int(input())
maps = []

for _ in range(0, N):
    row = list(map(int, input()))
    maps.append(row)

visited = [[0] * N for _ in range(0, N)]
def dfs(x_, y_, dangi):
    visited[y_][x_] = dangi
    cnt = 0
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x_ + i, y_ + j
        if 0 <= nx < N and 0 <= ny < N and maps[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[y_][x_] = dangi
            cnt +=1
            cnt += dfs(nx, ny, dangi)
    return cnt

dangi = 1
answer = []
for y in range(0, N):
    for x in range(0, N):
        if maps[y][x] == 1 and visited[y][x] == 0:
            cnt_ = dfs(x, y, dangi)
            answer.append(cnt_)
            dangi += 1
answer.sort()
print(len(answer))
for a in answer:
    print(a+1)
