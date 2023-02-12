# (0,0) 좌표와 가까운 K를 구하는 코드이다.
# 좌표간의 거리는 유클리디안 식을 사용한다.
# 최소 힙 트리를 구현하여 푼다.

import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for point in points:
            heapq.heappush(heap, (point[0]**2 + point[1]**2, point))
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result

if __name__ == "__main__":
    a = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2

    print(a.kClosest(points, k))