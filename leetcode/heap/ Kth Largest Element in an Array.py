import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-1 * num for num in nums]
        heapq.heapify(maxheap)
        for _ in range(k):
            result = heapq.heappop(maxheap)
        return -1 * result
        

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums, k))