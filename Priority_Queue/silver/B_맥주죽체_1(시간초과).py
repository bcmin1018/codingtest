# https://www.acmicpc.net/problem/17503
# 우선순위 큐
import heapq
N, M, K = map(int, input().split())
beers = []
for _ in range(0, K):
    beers.append(list(map(int, input().split())))

# 최소의 도수를 찾아야하므로 도수로 정렬
beers = sorted(beers, key=lambda x: (x[1], x[0]))

like_sum = 0
answer = 0
queue = []
for b in beers:
    like_sum += b[0]
    answer = max(answer, b[1])
    heapq.heappush(queue, b[0])
    if len(queue) == N:
        if like_sum >= M:
            print(answer)
            break
        else:
            min_like = heapq.heappop(queue)
            like_sum -= min_like
else:
    print(-1)


# 시간 초과가 계속 발생하는데 어떻게 풀까...

