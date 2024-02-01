def count_sort(arr, k):
    hash_table = [0] * (k+1)
    for num in arr:
        if num < k:
            hash_table[num] = 1
    return hash_table

def solution(arr, target):
    hash_table = count_sort(arr, target)

    for num in arr:
        key = target - num
        if hash_table[key] == 0:
            continue
        else:


arr = [1,2,3,4,8]
target = 6

solution(arr, target)
