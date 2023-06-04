# ㄱㅏ스 스테이션 중 한곳에서 비어있는 상태로 시작
# cost[i] 는 i ~ i+1 번 까지 가는 코스트
# i 번째 gas 보다 i + 1 cost가 크면 gas가 충분한지 확인해야한다.
# https://ihp001.tistory.com/124

class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_route = len(gas)
        total_gas = 0
        for i in range(0, total_route):
            if total_gas > 0:
                return i
            else:
                total_gas = 0
            total_gas = total_gas + gas[i]
            for j in range(i+1, total_route + i):
                if j > total_route-1:
                    total_gas += gas[j-total_route]
                    if total_gas - cost[j-total_route-1] < 0:
                        break
                    else:
                        total_gas = total_gas - cost[j-total_route-1]
                else:
                    if total_gas - cost[j-1] < 0:
                        total_gas = total_gas - cost[j-1]
                    else:
                        total_gas = total_gas - cost[j-1]
                    # total_gas += gas[j]
        return -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    a = Solution()
    print(a.canCompleteCircuit(gas, cost))
