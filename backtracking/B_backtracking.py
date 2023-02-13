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

def recur(num):
    if num == M: # 그래프의 깊이가 num과 동일하면 결과를 출력한다.
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1): # 자연수 for loop
        if chk[i] == False: # 방문하지 않았다면
            chk[i] = True # 방문 체크
            result.append(i) # 방문한 것을 result 배열에 입력
            recur(num+1) # 다음 depth를 탐색, 현재의 depth가 마지막 depth이면 return 후 다시 아래의 로직을 탄다.
            chk[i] = False # 방금 방문한 것을 삭제
            result.pop()

N, M = map(int, input().split()) #N; 자연수, M: 그래프에서의 깊이
result = []
chk = [False] * (N+1)
recur(0)