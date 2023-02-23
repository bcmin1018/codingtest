# https://www.youtube.com/watch?v=WUq13ACJmB8&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=4
# https://www.acmicpc.net/problem/15650
# 중복 된 요소를 제거해야하는 것이 이 문제의 포인트 인 것 같다. (1, 2), (2, 1)을 제거

import sys
sys.stdin = open("input.txt", "r")
#
# def dfs(n, lst):
#     if n == M:
#         ans.append(lst)
#         return
#     for c in range(1, N+1):
#         if v[c] == 0:
#             v[c] = 1
#             dfs(n+1, lst + [c])
#             v[c] = 0
#
#
# N, M = map(int, input().split())
# v = [0] * (N+1)
# ans = []
# dfs(0, [])
#
# ans2 = list([tuple(set(lst)) for lst in ans])
#
# for lst in ans2:
#     print(*lst)

# 위의 코드는 중복을 고려하지 않고 만든 코드이다.

def dfs(n, lst):
    global ans
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    # 포함을 할때
    dfs(n+1, lst + [n])

    # 포함을 하지 않을 때
    dfs(n+1, lst)

N, M = map(int, input().split())
# list_ = [i+1 for i in range(N)]
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)