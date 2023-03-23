class Solution:
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.answer = []
        self.lst = []
        self.dfs(0,0)
        return self.answer

    def dfs(self, n, sum):
        if sum > 7:
            # s += 1
            return

        if sum == 7:
            self.lst.append(candidates[n])
            self.answer.append(self.lst)
            self.lst = []
            # s += 1
            return

        if n > len(self.candidates)-1:
            return self.answer

        for c in range(len(self.candidates)):
            self.dfs(n+1, sum + self.candidates[c])

if __name__ == "__main__":
    a = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(a.combinationSum(candidates, target))
