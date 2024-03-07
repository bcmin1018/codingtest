#T : 테스트 케이스
#M : 배추밭 가로길이
#N : 배추밭 세로 길이
#K : 배추의 위치
T = int(input())
B = [[]] # 배추밭 배열
ck = [] # 완전 탐색시 방문했는지 체크 배열

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    ck[x][y] = 1 # 방문했다고 표시
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i] # 좌, 우, 상, 하 모두 탐색
        if B[xx][yy] == 0 or ck[xx][yy]: # 배추가 없거나 이미 방문한 곳이면 continue
            continue
        dfs(xx, yy)


def process():
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)] # 배추밭의 첫번째 좌표를 (1, 1)로 설정
    ck = [[0 for i in range(M+2)] for _ in range(N+2)] # 탐색이 완료된건지 체크하기 위함.
    for _ in range(K): # K : 배추의 개수
        X, Y = map(int, input().split())
        B[X+1][Y+1] = 1 #배추의 위치를 배추밭에 1로 표시한다. 배추밭의 처음 위치는 (0, 0) 이 아닌 (1, 1)로 설정.

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if ck[i][j] == 1: # 방문했다면 다음 loop를 돌기 대문에 continue 밑으로 내려가지 않는다.
                continue
            dfs(i, j) #방문하지 않았다면 그 지점에서 깊이 우선 탐색
            print(ans)
            ans += 1
    # print(ans)



for _ in range(T):
    process()

B = [[0 for i in range(4)] for _ in range(5)]
print(B)