# https://programmers.co.kr/skill_checks

# def solution(s):
#     answer = True
#     cnt = 0
#     lst = list(s)
#     for num in lst:
#         if num == 'y' or num == 'Y':
#            cnt +=1
#         elif num == 'p' or num == 'P':
#             cnt -= 1
#
#     if cnt == 0:
#         return answer
#
#     else:
#         answer = False
#         return answer

# print(solution('Pyy'))
import math


def solution(n):
    answer = 0
    for num in range(2, n+1):
        # for i in range(2, num):
        for i in range(2, int(math.sqrt(num) +1)):
            if num % i == 0:
                answer += 1
                break
    return n - answer -1

print(solution(5))

