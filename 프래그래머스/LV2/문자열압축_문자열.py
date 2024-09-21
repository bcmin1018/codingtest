# 제목 : 문자열 압축
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
# 설명
# 1. 중복되는 문자열의 뭉치들을 찾아야함.
#  -> 자르는 단위가 n인 경우 n을 1부터 하나씩 늘리면서 자른후 압축을 시도한다.
# 2. 중복되는 문자열 중 가장 긴 것을 찾는 것이 압축률을 높이는 방법
#  -> 꼭 그렇지많은 않다. 문자열이 짧으면서 똑같은 문자열이 반복적인 경우가 가장 높일 수 있기 때문이다.
# def solution(s):
#     slice_n = 1
#     answer = []
#     while slice_n <= (len(s) // 2):
#         temp = []
#         compressed = []
#         for i in range(0, len(s) + 1, slice_n):
#             strings = s[i:i + slice_n] # 이번 순서 문자열
#             if temp:
#                 if temp[-1] == strings:
#                     temp.append(strings)
#                     continue
#                 else:
#                     if len(temp) == 1:
#                         compressed.append(temp[0])
#                     else:
#                         compressed.append(str(len(temp)))
#                         compressed.append(temp[0])
#                     temp = []
#                     if len(strings) > 0:
#                         temp.append(strings)
#             else:
#                 temp.append(strings)
#         if len(temp) > 0:
#             compressed.append(temp[0])
#         slice_n += 1
#         answer.append(len(''.join(compressed)))
#     if len(answer) > 0:
#         return min(answer)
#     else:
#         return len(s)


def solution(s):
    if len(s) == 1:
        return 1

    slice_n = 1 # 자르는 문자열 개수 단위
    answer = []
    while slice_n <= (len(s) // 2): # 전체 문자열 길이의 반까지만 자른다.
        temp = []
        compressed = []
        for i in range(0, len(s) + 1, slice_n): # 부분 문자열
            strings = s[i:i + slice_n] # 이번 순서 문자열
            if temp:
                if temp[-1] == strings: # 부분 문자열 중복인 경우 temp 리스트로
                    temp.append(strings)
                    continue
                else: # 부분 문자열이 중복이 아닌 경우
                    if len(temp) == 1: # temp에 한가지의 문자열만 있는경우 (중복 X)
                        compressed.append(temp[0])
                    else: # temp에 한가지 이상의 문자열만 있는경우 (중복 O)
                        compressed.append(str(len(temp)))
                        compressed.append(temp[0])
                    temp = [] # temp 리셋
                    if len(strings) > 0: #부분 문자열이 있는경우에만
                        temp.append(strings)
            else:
                temp.append(strings) # 첫번재 부분 문자열
        if len(temp) > 0:
            compressed.append(temp[0])
        slice_n += 1
        answer.append(len(''.join(compressed)))
    return min(answer)


# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "ababcdcdababcdcd"
s = "a"
print(solution(s))