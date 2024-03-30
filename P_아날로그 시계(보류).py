#https://school.programmers.co.kr/learn/courses/30/lessons/250135
# 2024.03.30 실패
# 360도를 기준으로 얼마를 갈 수 있는지 구해야 한다.
def solution(h1, m1, s1, h2, m2, s2):
    answer = -1
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    if start == 0 or start == 12 * 3600:
        answer += 1
    # 속도
    ha, ma, sa = 1/60, 0.1, 1
    while start < end:
        n_h, n_m, n_s = start + ha, start + ma, start + sa


    return answer