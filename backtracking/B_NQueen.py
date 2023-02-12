# https://www.acmicpc.net/problem/9663

# 체스판에 몇개를 배치해야하나


# current_candidate : 이미 배치된 퀸의 배치 정보
# final_result : 전체 배치 정보


def is_available(candidate, current_col):
    current_row = len(candidate)

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N: # 종료 조건
        final_result.append(current_candidate)
        return

    for candidate_col in range(N): # 다음행을 체크
        if is_available(current_candidate, candidate_col): # current_candi
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop() # 백트레킹




def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result