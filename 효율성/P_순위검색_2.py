# 정확도는 통화했으나 효율성에서 통과하지 못함 순회를 3번 돌기 때문에 그러한 것 같음
# 점수로 미리 정렬하고 바이너리 서치를 하는 것은 어떨까?
# https://geunu97.tistory.com/56
# def solution(info, query):
#     rows = []
#     answer = []
#     for i in info:
#         row = []
#         rows.append(i.split())
#
#     new_query = []
#     for q in query:
#         new_q = [q_ for q_ in q.split() if q_ != 'and']
#         new_query.append(new_q)
#
#     for nq in new_query:
#         count = 0
#         for r in rows:
#             flag = True
#             if int(r[-1]) < int(nq[-1]):
#                 flag = False
#                 continue
#             else:
#                 for i in range(4):
#                     if nq[i] == "-":
#                         continue
#                     elif nq[i] != r[i]:
#                         flag = False
#                         break
#             if flag:
#                 count += 1
#         answer.append(count)
#     return answer

from collections import defaultdict

def all_cases(item):
    item = [i for i in item.split() if i != 'and']


def solution(info, query):

    for i in info:
        all_cases(i)
    # info의 모든 경우의 수를 구한다.
    # 점수를 value로 한 딕셔너리를 만든다.
    # query를 또 검색할 수 있는 경우의 수를 모두 구한다.
    # 해당 키를 확인한다.
    # 학인할때 바이너리 서치를 구한다.