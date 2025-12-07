from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = -1
        left_sum = 0
        right_sum = 0
        last_index = len(nums) -1
        
        for i in range(0, len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = sum(nums[i+1:last_index+1])
            elif i == last_index:
                left_sum = sum(nums[0:i])
                right_sum = 0
            else:  
                left_sum = sum(nums[0:i])
                right_sum = sum(nums[i+1:last_index+1])
            
            if left_sum == right_sum:
                pivot_index = i
                break
                
        return pivot_index
    
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))