# https://www.acmicpc.net/problem/14502
from collections import deque
def bfs(t_lst):
    # 벽 3개로 막기
    for i, j in t_lst:
        maps[i][j] = 1

    cnt = len(b_lst) -3
    q = deque()
    w = [[0] * M for _ in range(N)]
    for ti, tj in v_lst:
        q.append((ti, tj))
        w[ti][tj] = 1

        while q:
            ci, cj = q.popleft()
            for ii, jj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = ci+ii, cj+jj
                if 0<=ni<N and 0<=nj<M and w[ni][nj] == 0 and maps[ni][nj] == 0:
                    q.append((ni, nj))
                    w[ni][nj] = 1
                    cnt -=1
    # 벽 다시 해제
    for i, j in t_lst:
        maps[i][j] = 0
    return cnt

def dfs(n, t_lst):
    global ans
    if n == 3:
        ans = max(ans, bfs(t_lst))
        return
    for j in range(0, len(b_lst)):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, t_lst+[b_lst[j]])
            visited[j] = 0


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
b_lst = [] # 빈칸 위치
v_lst = [] # 바이러스 위치
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            b_lst.append((i, j))
        if maps[i][j] == 2:
            v_lst.append((i, j))

visited = [0] * len(b_lst)
ans = 0
dfs(0, [])
print(ans)







