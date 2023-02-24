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

def dfs(n, lst):
    if n == M: # 끝까지 다 탐색하지 않는다면 출력이 필요한 자리수까지가 종료 조건이 된다.
        ans.append(lst)
        return # ans 에 1,2를 업데이트하고 return이 된다.
    for c in range(1, N+1): # 루프를 돌며 방문을 체크하기 때문에 1, 1 과 같이 중복이 되는 것을 피할 수 있다.
        if v[c] == 0:
            v[c] = 1
            dfs(n+1, lst + [c]) # 현재 스택에서 lst는 1이기 때문에 위에서 return으로 돌아오는 경우 lst는 1인 상태가 된다.
                                # dfs 함수에 진입할때는 lst는 1,2로 진입 하게 된다..
            v[c] = 0 # v는 전역 변수여서 어느 함수에서든 표시를 할 수 있다. 따라서 재 방문을 위해 0으로 초기화 해야한다.

N, M = map(int, input().split()) # 4, 2
v = [0] * (N + 1)
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)

# def dfs(n, lst):
#     if n == M: # 재귀함수에서는 종료 조건을 항상 먼저 명시한다. 노드의 맨 끝에 닿을 경우 종료 조건을 발동시킨다.
#         ans.append(lst)
#         return
#
#     for c in range(1, N+1): # 아래의 노드를 탐색한다.
#         if v[c] == 0: # 방문했는지 확인한다.
#             v[c] = 1 # 방문 안했다면 방문 한 것을 체크 한다.
#             dfs(n+1, lst + [c]) # 다음 단계에서 아래 노드를 확인한다.
#             v[c] = 0 # 위에서 ans 리스트에 추가하고 리턴해서 빠져나오면 방문을 하지 않았다고 표시한다.
#                      # 같은 레벨의 다른 순번을 탐색하기 위해 필요한 절차이다.
#
# N, M = map(int, input().split()) #N; 자연수, M: 그래프에서의 깊이
# ans = [] # 정답 리스트
# v = [0] * (N+1) # 중복 확인 리스트
# dfs(0, [])
# for lst in ans:
#     print(*lst)

