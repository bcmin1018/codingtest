# 아직 풀지 못함.

class Solution:
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.answer = []
        self.dfs(0,0, [])
        return self.answer

    def dfs(self, n, sum, lst):
        if sum > 7:
            return

        if sum == 7:
            self.answer.append(lst)
            self.lst = []
            return
        #
        # if n > len(self.candidates)-1:
        #     return self.answer

        for c in range(0, len(self.candidates)-1):
            self.dfs(n+1, sum + self.candidates[c], lst + [candidates[c]])

if __name__ == "__main__":
    a = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(a.combinationSum(candidates, target))
