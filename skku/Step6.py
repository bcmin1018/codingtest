# 선택 정렬
# def ssort0(s):
#     global ans
#     if len(s) == 0:
#         return ans
#     else:
#         smallest = min(s)
#         s.remove(smallest)
#         ans.append(smallest)
#         return ssort0(s)
# ans = []
# print(ssort0([3,5,4,2]))

# 선택 정렬 꼬리 재귀
# 내가 짠코드
# def ssort1(lst, s):
#     if len(s) == 0:
#         return lst
#     else:
#         smallest = min(s)
#         s.remove(smallest)
#         return ssort1(lst + [smallest], s)
# print(ssort1([], [3,5,4,2]))

# 교수님이 짠 코드
def ssort1(s):
    def loop(s, slst):
        if s != []:
            smallest = min(s)
            s.remove(smallest)
            return loop(s, slst + [smallest])
        else:
            return slst
    return loop(s, [])

print(ssort1([3,5,4,2]))
