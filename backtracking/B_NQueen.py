# https://www.acmicpc.net/problem/9663
# https://www.youtube.com/watch?v=HRwFgtiqHH0

# 체스판에 몇개를 배치해야하나


# current_candidate : 이미 배치된 퀸의 배치 정보
# final_result : 전체 배치 정보


# def is_available(candidate, current_col):
#     current_row = len(candidate)
#
# def DFS(N, current_row, current_candidate, final_result):
#     if current_row == N: # 종료 조건
#         final_result.append(current_candidate)
#         return
#
#     for candidate_col in range(N): # 다음 행을 체크
#         if is_available(current_candidate, candidate_col): # current_candi
#             current_candidate.append(candidate_col)
#             DFS(N, current_row+1, current_candidate, final_result)
#             current_candidate.pop() # 백트레킹
#
# def solve_n_queens(N):
#     final_result = []
#     DFS(N, 0, [], final_result)
#     return final_result


def n_queens(i, col):
    # i = depth col = 칼럼 배열
    n = len(col) -1
    if (promising(i, col)):
        if i == n: # 아래 depth까지 탐색
            print(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising (i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False # 유망하지 않다는 뜻이다.
        k += 1
    return flag

n = 4
col = [0] * (n + 1)
n_queens(0, col)



