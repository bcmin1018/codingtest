class Solution:
    def maxDepth(self, root) -> int:
        depth = 0
        for i in range(0, len(root)+1, 2**2):

            depth+=1
        return depth+1

if __name__ == "__main__":
    a = Solution()
    # lst = [3,9,20,'null','null',15,7]
    lst = [3,9,20,'null','null',15,7]
    print(a.maxDepth(lst))