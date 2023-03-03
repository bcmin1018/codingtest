# 너무 어렵게 풀었다.

import sys
sys.stdin = open("input.txt", "r")

# n = int(input())
# sum_ = 0
# score = 0
#
# def scoring(idx, lst):
#     global score
#     global sum_
#
#     if idx == len(lst):
#         print(sum_)
#         sum_ = 0
#         score = 0
#     else:
#         if lst[idx] == 'X':
#             score = 0
#         else:
#             score += 1
#             sum_ += score
#
# for _ in range(n):
#     lst = list(input())
#     for idx in range(0, len(lst) +1):
#         scoring(idx, lst)


n = int(input())
for _ in range(n):
    lst = list(input())
    score = 0
    sum_score = 0
    for c in lst:
        if c == 'O':
            score += 1    # 스코어를 일 더한다. 다음 번에도 O 가 나오면 스코어는 2가 된다.
            sum_score += score
        else:
            score = 0

    print(sum_score)