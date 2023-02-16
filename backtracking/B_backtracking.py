# https://www.acmicpc.net/problem/15649
# 시간 복잡도 중복이 가능한 경우 N**N, 중복이 불가하면 N!
# 1. 아이디어
# - 백트레킹 재귀함수 안에서, for 돌면서 숫자 선택
# - 재귀함수에서 M개를 선택할 경우 print
# 2. 시간복잡도: N!
# 3. 자료구조
# - 방문 여부 확인 배열 : bool
# - 선택한 값 입력 배열 : int


import sys
sys.stdin = open("input.txt", "r")

# def recur(num):
#     if num == M: # 그래프의 깊이가 num과 동일하면 결과를 출력한다.
#         print(' '.join(map(str, result)))
#         return
#     for i in range(1, N+1): # 자연수 for loop
#         if chk[i] == False: # 방문하지 않았다면
#             chk[i] = True # 방문 체크
#             result.append(i) # 방문한 것을 result 배열에 입력
#             recur(num+1) # 다음 depth를 탐색, 현재의 depth가 마지막 depth이면 return 후 다시 아래의 로직을 탄다.
#             chk[i] = False # 방금 방문한 것을 삭제
#             result.pop()
#
# N, M = map(int, input().split()) #N; 자연수, M: 그래프에서의 깊이
# result = []
# chk = [False] * (N+1)
# recur(0)

def dfs(n, lst):
    if n == M: # 재귀함수에서는 종료 조건을 항상 먼저 명시한다. 노드의 맨 끝에 닿을 경우 종료 조건을 발동시킨다.
        ans.append(lst)
        return

    for c in range(1, N+1): # 아래의 노드를 탐색한다.
        if v[c] == 0: # 방문했는지 확인한다.
            v[c] = 1 # 방문 안했다면 방문 한 것을 체크 한다.
            dfs(n+1, lst + [c]) # 다음 단계에서 아래 노드를 확인한다.
            v[c] = 0 # 위에서 ans 리스트에 추가하고 리턴해서 빠져나오면 방문을 하지 않았다고 표시한다.
                     # 같은 레벨의 다른 순번을 탐색하기 위해 필요한 절차이다.

N, M = map(int, input().split()) #N; 자연수, M: 그래프에서의 깊이
ans = [] # 정답 리스트
v = [0] * (N+1) # 중복 확인 리스트
dfs(0, [])
for lst in ans:
    print(*lst)

