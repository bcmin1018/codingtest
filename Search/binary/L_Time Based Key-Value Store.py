# https://leetcode.com/problems/time-based-key-value-store/
# 바이너리서치로 찾으려는 key값 보다 작은 값 중에 가장 작은 값을 찾는 것.
class TimeMap:
    def __init__(self):
        self.dict = {}
        self.tsList = []

        # {
        #   "foo":
        #      {
        #          '1' : 'bar',
        #          '4' : 'bar2'
        #      }
        #  }
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tsList.append(timestamp)
        sorted(self.tsList)
        if self.dict.get(key) == None:
            self.dict[key] = {}
            self.dict[key][timestamp] = value
        else:
            self.dict[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        if timestamp not in self.dict[key].keys():
            close_num = self.binary_search_closest(self.tsList, timestamp)
            return self.dict[key][close_num]
        return self.dict[key][timestamp]
    def binary_search_closest(self, arr, target):
        low = 0
        high = len(arr) - 1
        closest = None
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                closest = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return closest

if __name__ == "__main__":
    obj = TimeMap()
    obj.set('foo','bar2',4)
    parma_1 = obj.get('foo',4)
    print(parma_1)
    param_2 = obj.get('foo', 5)
    print(param_2)

# 예시 배열
# numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 가장 가까운 숫자 찾기
# target = 12
# closest_number = binary_search_closest(numbers, target)
# print(f"가장 가까운 숫자: {closest_number}")