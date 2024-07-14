#https://school.programmers.co.kr/learn/courses/30/lessons/258709?language=python3
from itertools import combinations

def dfs(n, dice1, dice2, exit):
    if n == exit:
        return


def solution(dice):
    n = len(dice)
    cases = list(combinations(dice, n//2))
    for case in cases:
        dfs(n, )
    answer = []
    return answer

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

solution(dice)
