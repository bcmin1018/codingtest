# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# https://www.youtube.com/watch?v=qSmxC1HgRMY&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=6

import sys
sys.stdin = open('input.txt', 'r')

#  cnt 교환 횟수

def dfs(n, cnt):
    global ans

    if ans <= cnt-1:
        return

    # 정류장을 이미 지나쳤다면
    if n >= N-1:
        ans = min(ans, cnt-1)
        return ans

    # 다음 정류장에서 배터리를 교체 했을때 경유한 정류장 수는 1을 추가하고 배터리 수만큼 점프한다.
    dfs(n + bat[n], cnt + 1)
    # 배터리 교체를 하지 않으면 바로 다음 정류장으로 이동한다.
    dfs(n + 1, cnt + 1)


T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N
    dfs(2, 0)
    print(f'#{test_case} {ans}')