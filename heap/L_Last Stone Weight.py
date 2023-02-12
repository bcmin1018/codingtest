# stone 배열 중에 가장 큰 두개의 값을 선택한다.
# 큰 두개의 stone을 서로 충돌 시킨다.
# 두개의 스톤 값이 같으면 두개다 없어지고 하나가 크면 차액만 남는다.
# 힙을 이용하여 배열에서 큰 두개의 값을 구하고 이후 로직에 태우자.
# 두개의 차이를 다시 힙에 넣으면 되는데 쓸데없이 어렵게 품.

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) != 1:
            y, x = self.heapify(stones) # stone 배열을 최대 힙정렬 하고 최대 2개의 값을 뽑아낸다.
            if x[1] == y[1]:
                if len(stones) == 2:
                    return 0
                else:
                    if y[2] > x[2]:
                        del stones[y[2]]
                        del stones[x[2]]
                    else:
                        del stones[x[2]]
                        del stones[y[2]]
            else:
                if y[1] > x[1]:
                    smash = y[1] - x[1]
                    stones[y[2]] = smash
                    del stones[x[2]]
                else:
                    smash = x[1] - y[1]
                    stones[x[2]] = smash
                    del stones[y[2]]
        return stones[0]

    def heapify(self, list):
        heap = []
        for i, weight in enumerate(list):
            heapq.heappush(heap, (-weight, weight, i)) # index도 함께 입력
        y = heapq.heappop(heap) # 가장 큰값
        x = heapq.heappop(heap) # 두번째 큰값
        return y, x


if __name__ == "__main__":
    a = Solution()
    # stones = [2,7,4,1,8,1]
    stones = [2, 2]
    print(a.lastStoneWeight(stones))