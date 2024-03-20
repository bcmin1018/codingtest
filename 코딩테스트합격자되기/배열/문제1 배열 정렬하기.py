def solution(arr):
    arr.sort()
    arr.sort(reverse=True)
    return arr

arr = [2, 1, 1, 3, 2, 5, 4]
print(solution(arr))