#https://www.acmicpc.net/problem/18429
#운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력하는 프로그램을 작성하시오.

N, K = map(int, input().split())
kit = list(map(int, input().split()))
visited = [0] * N
cnt = 0
def dfs(max, n):
    global cnt
    if max < 500:
        return

    if n == N:
        cnt += 1
        return

    max = max - K
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(max+kit[i], n+1)
            visited[i] = 0

dfs(500, 1)
print(cnt)