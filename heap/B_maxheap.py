# https://www.acmicpc.net/problem/11279
# 해시맵을 만드는데 시간 복잡도 O(n)
# 런타임 에러 발생. 이유 모름.

import sys
import heapq
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            mx = heapq.heappop(heap)
            print(mx[1])
    else:
        heapq.heappush(heap, (-x, x))


# import heapq
# from collections import defaultdict
#
# nums = [1, 3, 5, 3, 9, 3, 7, 5]
# k = 2
# dic = defaultdict(int)
# for num in nums:
#     dic[num] += 1
#
# topK_heap = []
# for num in dic:
#     heapq.heappush(topK_heap, (dic[num], num))
#     if k < len(topK_heap):
#         heapq.heappop(topK_heap)








