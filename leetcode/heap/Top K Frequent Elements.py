import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # O(n) iterate over nums
        heap = [(-freq, num) for num, freq in counter.items()] #O (n)
        heapq.heapify(heap) # O(n)
        
        result = []
        for _ in range(k):
            most_frequent = heapq.heappop(heap) # O(log n) * k   after pop, reorder heap.
            result.append(most_frequent[1])
        return result
    
nums = [1,1,1,2,2,3]
k = 2
print(Solution().findKthLargest(nums, k))