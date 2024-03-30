# def solution(citations):
#     answer = 0
#     cnt = 0
#     n = len(citations)
#     h = 0
#
#     while True:
#         for citation in citations:
#             if citation >= h:
#                 cnt += 1
#         if h == cnt:
#             answer = cnt
#             break
#         h += 1
#         cnt = 0
#
#     return answer
