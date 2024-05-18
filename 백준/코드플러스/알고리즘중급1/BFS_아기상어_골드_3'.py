# https://www.acmicpc.net/problem/16236
# https://www.youtube.com/watch?v=zWH959IBv-I
# 먹을 대상이 여러개인 경우 발견 즉시 먹는 것이 아니라 리스트에 좌표를 입력하고 정해준 순서에 따라 먹도록 한다.
from collections import deque
def bfs(x, y):
    queue = deque()
    v = [[0] * N for _ in range(N)]
    tlst = []
    dist = 0

    queue.append((x, y))
    v[y][x] = 1
    while queue:
        cx, cy = queue.popleft()
        if dist == v[cy][cx]:
            return tlst, dist -1

        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx + i, cy + j
            if 0<=nx<N and 0<=ny<N and v[ny][nx] == 0 and maps[ny][nx] <= shark:
                queue.append((nx, ny))
                v[ny][nx] = v[cy][cx] + 1
                if 0< maps[ny][nx] < shark:
                    tlst.append((nx, ny))
                    dist = v[ny][nx]

    return tlst, dist-1


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if maps[y][x] == 9:
            cx, cy = x, y
            maps[y][x] = 0

shark = 2
answer = 0
cnt = 0
while True:
    tlst, dist = bfs(cx, cy) #처음 시작 위치에서 먹을 수 있는 물고기 좌표와 움직인 거리를 반환한다.
    if len(tlst) == 0: #먹을 물고기가 없다면 종료하고 움직인 거리 반환
        break
    tlst.sort(key=lambda x:(x[1], x[0]))
    cx, cy = tlst[0]
    maps[cy][cx] = 0 #물고기를 먹었다.
    cnt += 1
    answer += dist
    if shark == cnt:
        shark += 1
        cnt = 0
print(answer)