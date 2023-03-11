# https://www.youtube.com/watch?v=iDyzoCtblls&list=PLodgw23vNd_U66omABrprSwJBZhKPFGMM&index=3
# 특정 높이 B 에 있는 선반을 끄내기 위해 직원들의 합친 키를 최소한으로 하는 문제.
# 가능한 모든 경우의 수를 구한다.
# dfs 가능한 모든 경우의 수를 구하다가 최소 값보다 큰면 가지치기
# 첫번쨰 사람을 포함하지 않을 수도 있기 때문에 이진트리로 풀어야한다.
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm):
    global ans
    if ans <= sm - shelf_H:
        return

    if n == num:
        if sm >= shelf_H:
            ans = min(ans, sm - shelf_H)
        return

    dfs(n+1, sm + clerk_H[n])
    dfs(n+1, sm)

T = int(input())
for test_case in range(1, T+1):
    num, shelf_H = map(int, input().split())
    clerk_H = list(map(int, input().split()))
    ans = num * 10000
    dfs(0, 0)
    print(f'#{test_case} {ans}')