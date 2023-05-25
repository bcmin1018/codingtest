# https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 1 ~ 최대 길이 까지 루프를 돌며 각 번호에 요격할 수 있는 target을 선정.
# x 좌표에 따라 요격이 가능한 미사일을 나열한다.
# 미사일을 가장 많이 요격할 수 있는 x 좌표외의 좌표는 모두 삭제한다.
# set 을 사용한 교집합으로 문제 접근
lst1 = ['A', 'B', 'C', 'D']
lst2 = ['C', 'D', 'E', 'F']
print(set(lst1) & set(lst2))

def solution(targets):
    min_ = 1
    max_ = 0

    for target in targets:
        if target[1] > max_:
            max_ = target[1]

    print(max_)







    answer = 0
    return answer