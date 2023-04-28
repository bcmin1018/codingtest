# https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EA%B7%A4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-Python

# 귤의 크기는 중요하지 않고 개수가 중요하다.
# 서로 다른 종류가 최소가 되게 하기 위해서는 개수가 많은 숫자부터 k에 담아야한다.

def solution (k, tangerine):
    answer = 0
    dic = {}
    # 딕셔너리를 세팅한다
    for key in tangerine:
        dic[key] = 0
    # 딕셔너리에 값을 넣는다.
    for key in tangerine:
        dic[key] += 1
    # dic.item에서 value를 key로 하여 내림차순 정렬한다.
    lst = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    # value를 뽑아 k 값에서 빼주고 k가 0<으면 리턴한다.
    for _, value in lst:
        if k > 0:
            k = k - value
            answer += 1
        else:
            break
    return answer

print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))