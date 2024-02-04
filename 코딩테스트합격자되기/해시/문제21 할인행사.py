# def solution(want, number, discount):
#     dic = {}
#     for w, n in zip(want, number):
#         dic[w] = n
#
#     iter = len(discount) - 10 + 1
#     answer = 0
#     for i in range(0, iter):
#         n_dic = dic.copy()
#         for d in discount[0+i : 10+i]:
#             if d in n_dic:
#                 n_dic[d] -= 1
#
#         buy_all = True
#         for key in n_dic.keys():
#             if n_dic[key] != 0:
#                 buy_all = False
#
#         if buy_all:
#             answer += 1
#     return answer

def solution(want, number, discount):
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n
    iter = len(discount) - 10 + 1
    answer = 0
    for i in range(0, iter):
        dic_10d = {}
        for d in discount[0+i : 10+i]:
            if d in dic_10d:
                dic_10d[d] += 1
            else:
                dic_10d[d] = 1
        if dic == dic_10d:
            answer += 1
    return answer



w = ["banana", "apple", "rice", "pork", "pot"]
n = [3, 2, 2, 2, 1]
d = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

# w = ["apple"]
# n = [10]
# d = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(w, n ,d))



