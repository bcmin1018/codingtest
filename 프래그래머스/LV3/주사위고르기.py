#https://school.programmers.co.kr/learn/courses/30/lessons/258709?language=python3
from itertools import combinations, product

def binary_search(case, target):
    s, e = 0, len(case)-1
    while s<=e:
        m = (s + e) // 2
        if case[m] < target:
            s = m + 1
        else:
            e = m - 1
    return s


def solution(dice):
    n = len(dice)
    cases = list(combinations(range(0, n), n//2))

    A = []
    for case in cases:
        dices = [dice[i] for i in case]
        sums = sorted([sum(case_tuple) for case_tuple in list(product(*dices))])
        A.append(sums)

    answer = []
    b_sum = 0
    for i in range(len(A)):
        B = A[len(A)-i-1]
        t_sum = 0
        for t in A[i]:
            t_sum += binary_search(B, t)

        if t_sum > b_sum:
            b_sum = t_sum
            answer = [x+1 for x in cases[i]]

    return answer

# dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
# dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
print(solution(dice))
