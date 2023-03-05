import copy

class Solution(object):
    def cloneGraph(self, node):
        deep_copy = copy.deepcopy(node)
        return deep_copy


if __name__ == "__main__":
    input = [[2,4],[1,3],[2,4],[1,3]]
    a = Solution()
    print(a.cloneGraph(input))
