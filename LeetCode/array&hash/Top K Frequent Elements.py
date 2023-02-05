# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict
# nums = [1,1,1,2,2,3]
nums = [1,2]
k = 2

class Solution(object):
    def topKFrequent(self, nums, k):
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        ans = [ k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:k]] # dic 를 value를 기준으로 정렬
        return ans

if __name__ == "__main__":
    a = Solution()
    print(a.topKFrequent(nums, k))