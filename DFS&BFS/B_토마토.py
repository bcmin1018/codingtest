# https://www.acmicpc.net/problem/7569
# 상, 하, 좌, 우, 앞, 뒤 총 6면을 탐색한다.
# 한번 다 탐색하면 일수 + 1
# 방문하면 방문한 일자로 visited 배열을 update
# !주변을 방문했을 때 하루가 지나는 방식이므로 BFS가 적절
import sys

sys.stdin = open("input.txt", "r")

from collections import deque
def bfs():
    q = deque()

    # 익은 토마토의 좌표를 q에 삽입, -1 토마토를 빼기 위해 대상에서 제외 해야한다.
    # 안익은 토마토 0을 카운트하여 익었을때 -1을 해준다.
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == 1: # 익은 사과를 찾았을 경우
                    visited[h][i][j] = 1 # 몇일차 방문 표시
                    q.append((h, i, j))
                elif box[h][i][j] == 0: # 덜 익은 사과를 찾은 경우
                    cnt +=1 # 카운트를 한다.

    while q:
        ch, ci, cj = q.popleft() # 익은 사과의 현재 좌표
        for h, i, j in ((0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)):
            nh, ni, nj = ch + h, ci + i, cj + j
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and visited[nh][ni][nj] == 0 and box[nh][ni][nj] == 0:
                visited[nh][ni][nj] += visited[ch][ci][cj] + 1 # 익은 사과의 주변을 모두 몇일차 방문인지 표시
                q.append((nh, ni, nj)) # 방문 안한 곳은 큐에 삽입
                cnt -= 1 # 방문한 것은 즉 익었다는 의미이므로 안익은 사과의 카운트를 -1
    if cnt == 0:
        return visited[ch][ci][cj] -1
    return -1

M, N, H = map(int, input().split()) # M 가로, N 세로
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M  for _ in range(N)] for _ in range(H)]

ans = bfs()
print(ans)
