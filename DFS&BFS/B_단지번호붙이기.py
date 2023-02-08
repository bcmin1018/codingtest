# https://www.acmicpc.net/problem/2667
# https://www.youtube.com/watch?v=JOZmWQHXQ1E&list=PLodgw23vNd_VTBKHg-WgxQSD_wTPgtyzN&index=4

# 맵의 크기가 커지는 경우 DFS는 파이썬의 스택 제한이 있으므로 BFS로 문제를 푸는 것이 좋다.
# 군집 형태로 되어 있는 경우 전체 맵을 돌면서 방문하지 않았던 곳을 만나면 BFS를 타는 형식으로 한다.
# 방문하지 않은 곳에서 BFS를 탔지만 단지가 아니라면 빠져나오기 때문이다.
import sys
sys.stdin = open("input.txt", "r")

def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.pop(0)
        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + i, cj + j
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] == 1:
                v[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if v[i][j] == 0 and arr[i][j] == 1: # 방문하지 않고 아파트가 있으면 BFS를 탄다.
            ans.append(bfs(i,j))

ans.sort()
print(len(ans), *ans, sep='\n')


