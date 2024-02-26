# https://www.acmicpc.net/problem/11279
import sys
import heapq

n = int(input())

max_heap = []

for _ in range(n):
    h = int(sys.stdin.readline())
    if h == 0 and len(max_heap) == 0:
        print(0)
    elif h==0 and len(max_heap) != 0:
        print(-heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-h, -h))