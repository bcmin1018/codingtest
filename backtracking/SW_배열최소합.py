# https://www.youtube.com/watch?v=UTUShCoTPaM&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=2
# 가치 치기를 위해 v 배열을 사용. 같은 세로에 숫자를 중복으로 선택할 수 없다. 따라서 길이와 동일한 배열을 생성하고 체크한다.

import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm):
    global ans

    if ans <= sm: # 기존의 닶보다 값이 작으면
        return

    if n == N: # 종료 조건
        ans = min(ans, sm)
        return

    for j in range(0, N):
        if v[j] == 0: # 방문하지 않았다면
            v[j] = 1 # 방문 표시
            dfs(n+1, sm+arr[n][j]) # 깊이 탐색
            v[j] = 0 # 빠져나오면서 방문 표시 해제


T = int(input()) # 총 테스트 케이스 수
for test_case in range(1, T+1):
    N = int(input()) # 가로 X 세로
    arr = list(list(map(int, input().split())) for _ in range(N))
    ans = N * 10
    v = [0] * N
    dfs(0, 0)
    print(f'#{test_case} {ans}')
