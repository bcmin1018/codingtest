# https://www.acmicpc.net/problem/17503
# 우선순위 큐
import heapq
N, M, K = map(int, input().split()) #N: 열리는 기간, M: 선호도 합 K: 맥주 종류의 수
beers = []
max_ = 0
for _ in range(0, K):
    beer = list(map(int, input().split()))
    if beer[1] > max_:
        max_ = beer[1]
    beers.append(beer)

# 최소의 도수를 찾아야하므로 도수로 오름차순 정렬
# beers = sorted(beers, key=lambda x: (x[1], x[0]))
#
# like_sum = 0
# answer = 0
# queue = []
# for b in beers:
#     like_sum += b[0]
#     answer = max(answer, b[1])
#     heapq.heappush(queue, b[0])
#     if len(queue) == N:
#         if like_sum >= M:
#             print(answer)
#             break
#         else:
#             min_like = heapq.heappop(queue)
#             like_sum -= min_like
# else:
#     print(-1)


# 시간 초과가 계속 발생하는데 어떻게 풀까... 조건에 맞는 것 중에 도수의 최소값을 구하는 방식 -> 이분 탐색 lower bound
# 이렇게 변경했는데 계속 시간 초과.. 뭐가 문제일까
beers = sorted(beers, key=lambda x: x[0])
left, right = 0, max_
result = -1
while left <= right:
    mid = (left+right) // 2
    likes = [beer[0] for beer in beers if beer[1] <= mid]
    total = sum(likes[-N:])
    if total >= M:
        right = mid - 1
        result = right + 1
    else:
        left = mid + 1
print(result)




