# https://www.youtube.com/watch?v=WUq13ACJmB8&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=4
# https://www.acmicpc.net/problem/15650
# 중복 된 요소를 제거해야하는 것이 이 문제의 포인트 인 것 같다. (1, 2), (2, 1)을 제거

import sys
sys.stdin = open("input.txt", "r")
def dfs(n, lst):
    if n == N+1: # 기본적으로 끝까지 탐색을 위해 제시된 노드와 비교
        if len(lst) == M:
            ans.append(lst)
        return
    dfs(n+1, lst + [n])
    dfs(n+1, lst)

N, M = map(int, input().split()) # 4, 2
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)

# 위의 코드는 중복을 고려하지 않고 만든 코드이다.

# def dfs(n, lst):
#     global ans
#     if n > N:
#         if len(lst) == M:
#             ans.append(lst)
#         return
#     # 포함을 할때
#     dfs(n+1, lst + [n])
#
#     # 포함을 하지 않을 때
#     dfs(n+1, lst)
#
# N, M = map(int, input().split())
# # list_ = [i+1 for i in range(N)]
# ans = []
# dfs(1, [])
# for lst in ans:
#     print(*lst)