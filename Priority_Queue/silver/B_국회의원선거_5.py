import heapq
N = int(input())
rep = [int(input()) for _ in range(0, N)]
me = rep[0]
answer = 0
heap= []
for r in rep[1:]:
    heapq.heappush(heap, -r)

while len(heap) > 0:
    max_ = -heapq.heappop(heap)
    if me > max_:
        break
    heapq.heappush(heap, -(max_-1))
    me+=1
    answer += 1
print(answer)