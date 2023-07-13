class Solution(object):
    def minEatingSpeed(self, piles, h):
        hours = 0
        min_ = sum(piles) / 1
        for k in range(1, h+1): # 한시간에 먹는 양을 늘린다.
            for pile in piles:
                hour = pile // k # i 번째 pile를 다 먹는데 걸리는 시간
                hours += hour
                if hours > h: # 경비원이 돌아오면
                    break



if __name__ == "__main__":
    # print(3 % 4)
    piles = [3,6,7,11]
    h = 8
    a = Solution()
    a.minEatingSpeed(piles, h)
    print(a)