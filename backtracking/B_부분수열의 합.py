# https://www.acmicpc.net/problem/1182
# https://www.youtube.com/watch?v=4EAg1Pmk3bw&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=3
# 그래프 구조를 통해 포함 1 비포함 2 두개를 백트레킹으로 찾아가는 문제.

import sys
sys.stdin = open ("input.txt", "r")

def dfs(n, sum, cnt):
    global ans # 경우의 수
    if n == N: # 맨 아래까지 내려가면 종료 조건, 포함을 하거나 하지 않아도 n은 5까지 내려간다.
        if sum == S and cnt > 0: # 종료 조건일 경우 sum과 cnt가 조건에 맞으면 경우의 수 하나를 추가.
            ans += 1
        return # 종료 조건에 부합되지 않으면 dfs를 빠져나가 위의 노두에서 포함하지 않는 경우로 간다.

    # 하부함수 호출
    # 포함하는 경우
    dfs(n+1, sum + lst[n], cnt+1) # 포함하는 경우에는 다음 노드로 가기 위한 n+1을 하고, sum을 늘린다.
    # 포함하지 않은 경우 (sum과 cnt는 그대로 다음 노드에 전달해준다.)
    dfs(n+1, sum, cnt) # 포함하지 않는 경우에는 다음 노드로 가지만 sum을 추가 하지 않는다.

N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)

