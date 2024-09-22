# 제목 : 가장 많이 받은 선물
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 풀이 접근
# 1. 주고받은 선물의 개수와 지수를 잘 표현하는 자료 구조를 선정
# -> 이름이 고유하기 때문에 "준사람 받은사람" : 2 와 같이 표현한다.
# 2. 두사람이 선물을 주고 받은 기록이 있는지 확인
# -> 있으면 많이 준 사람이 하나를 받는다.
# -> 없거나 주고 받은 기록이 같다면 선물 지수가 큰 사람이 받는다.

from collections import defaultdict
import itertools
def solution(friends, gifts):
    gift_map = defaultdict(int)

    for u1, u2 in itertools.product(friends, repeat=2):
        if not gift_map[u1 + " " + u2]:
            gift_map[u1 + " " + u2] = 0

    for gift in gifts:
        gift_map[gift] += 1

    gift_index = defaultdict(int)
    for friend in friends:
        give = 0
        take = 0
        for k, v in gift_map.items():
            if k.split()[0] == friend:
                give += v
            if k.split()[1] == friend:
                take += v
        index = give - take
        gift_index[friend] = index
    # print(gift_index)
    combinations = list(itertools.combinations(friends, 2))

    result = defaultdict(int)
    for c in combinations:
        key1, key2 = c[0] + " " + c[1], c[1] + " " + c[0]
        if gift_map[key1] + gift_map[key2] > 0: # 두사람이 선물을 주고 받은 기록이 있다면
            if gift_map[key1] > gift_map[key2]: # a가 더 큰 경우
                result[c[0]] += 1
            elif gift_map[key1] < gift_map[key2]: # b가 더 큰 경우
                result[c[1]] += 1
            else: # 주고 받은 기록이 같다면
                if gift_index[c[0]] > gift_index[c[1]]:
                    result[c[0]] += 1
                elif gift_index[c[0]] < gift_index[c[1]]:
                    result[c[1]] += 1
        else:
            if gift_index[c[0]] > gift_index[c[1]]:
                result[c[0]] += 1
            elif gift_index[c[0]] < gift_index[c[1]]:
                result[c[1]] += 1
    answer = 0
    for k, v in result.items():
        answer = max(answer, v)
    return answer

# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# friends = ["a", "b", "c", "d"]
# gifts = ["c d", "c d"]

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]


print(solution(friends, gifts))
