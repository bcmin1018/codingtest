# https://leetcode.com/problems/time-based-key-value-store/
# class TimeMap:
#
#     def __init__(self):
#         self.dict = {}
#
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if self.dict.get(key) == None:
#             self.dict[key] = {}
#             self.dict[key][timestamp] = value
#         else:
#             self.dict[key][timestamp] = value
#
#     def get(self, key: str, timestamp: int) -> str:
#         return self.dict[key][timestamp]
#
#
# if __name__ == "__main__":
#     obj = TimeMap()
#     obj.set('foo','bar',1)
#     param_2 = obj.get('foo',1)
#     print(param_2)


def binary_search_closest(arr, target):
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

# 예시 배열
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 가장 가까운 숫자 찾기
target = 12
closest_number = binary_search_closest(numbers, target)
print(f"가장 가까운 숫자: {closest_number}")