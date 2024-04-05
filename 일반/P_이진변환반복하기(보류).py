# 제거한 0의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = []
    remove = 0
    # print(s)
    while len(s) > 1:
        s = list(s)
        for i, s_ in enumerate(s):
            print(s, s_)
            if s_ == "0":
                remove += 1
                del s[i]
        print(s)
        print(len(s))
        s = bin(len(s))
        print(s)
        break
    return answer

s = "110010101001"
solution(s)