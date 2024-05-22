from itertools import combinations_with_replacement

def find_hightest_list(lsts):
    result = None
    max_index = -1
    max_value = 0
    for lst in lsts:
        for i, n in enumerate(lst):
            if n > 0 and i >= max_index:
                max_index = i
                if lst[i] > max_value:
                    max_value = lst[i]
                    result = lst
                result = lst
    return result

def score(apeach, ryan):
    target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    target_ryan = [0] * 11
    for r in ryan:
        target_ryan[-r-1] += 1

    sum_a, sum_r = 0, 0
    for i, (a, r) in enumerate(zip(apeach, target_ryan)):
        if r == 0 and a == 0:
            continue
        if r<=a:
            sum_a += target[i]
        elif a<r:
            sum_r += target[i]
    return sum_r - sum_a, target_ryan


def solution(n, info):
    v = [0] * n
    ryan = list(combinations_with_replacement(
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        n)
    )

    # def dfs(step, ryan, info):
    #     global answer
    #     if n == step:
    #         return
    #     for i in range(0, 12):
    #         if v[step] == 0:
    #             v[step] = 1
    #             score_gap, target_ryan = score(info, ryan)
    #             if max_gap < score_gap:
    #                 max(max_gap, score_gap)
    #                 answer = score_gap
    #             dfs(step, ryan, info)
    #             v[step] = 0

    max_gap = 0
    answer = []
    for r in ryan:
        score_gap, target_ryan = score(info, r)
        if score_gap> 0:
            answer.append((score_gap, target_ryan))
        # if max_gap < score_gap:
        #     max_gap = score_gap
        #     answer.clear()
        #     answer.append(target_ryan)
        # elif max_gap == score_gap:
        #     answer.append(target_ryan)

    if len(answer) == 0:
        return [-1]
    else:
        result = sorted(answer, reverse=True)
        return result[0]

# print(find_lowest_scoring_list([[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1])) # [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

# print(score([0,0,1,2,0,1,1,1,1,1,1], (10, 9, 8, 8, 7, 7, 7, 5, 5)))
# print(score([0,0,1,2,0,1,1,1,1,1,1], (10, 9, 8, 8, 6, 5, 5, 4, 4)))