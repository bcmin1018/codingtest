import sys
sys.stdin = open("input.txt", "r")

# def bfs(si, sj, ei, ej):
#     q = []  #큐 생성
#     v = [[0] * M for _ in range(M)] # 방문 배열 생성
#     q.append((si, sj)) #큐에 시작 좌표 넣고
#     v[si][sj] = 1 #시작 좌표 방문 표시
#
#     while q:
#         ci, cj = q.pop(0) # 현재 좌표
#
#         if (ci, cj) == (ei, ej): # 현재 좌표와 종료 좌표 비교
#             return v[ei][ej]
#
#         # 4방향 범위내 조건에 맞으면 큐에 삽입
#         for di, dj in ((-1,0), (1,0), (0, -1), (0, 1)): # 상하좌우 방향
#             ni, nj = ci+di, cj+dj # 주변 탐색 대상 좌표
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and v[ni][nj] == 0:
#                 q.append((ni, nj)) # 조건에 부합하면 큐에 삽입
#                 v[ni][nj] = v[ci][cj] + 1 # 현재 좌표에 있는 값 + 1하여 새로운 값에 추가
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
#
# ans = bfs(0, 0, N-1, M-1)
# print(ans)


def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        if (ci, cj) == (ei, ej):
            return v[ei][ej]

        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci+i, cj+j
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] ==1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs(0, 0, N-1, M-1)
print(ans)
