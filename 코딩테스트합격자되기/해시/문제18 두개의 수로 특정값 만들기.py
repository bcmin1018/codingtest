def count_sort(arr, k):
    hash_table = [0] * (k+1)
    for num in arr:
        if num < k:
            hash_table[num] = 1
    return hash_table

def create_hash_table(arr):
    hash_table = [0] * (max(arr) + 1)
    for num in arr:
        hash_table[num] = 1
    return hash_table


def solution(arr, target):
    # hash_table = count_sort(arr, target)
    answer = False
    hash_table = create_hash_table(arr)
    for num in arr:
        key = target - num
        if hash_table[key] == 1 and key != num:
            answer = True

    return answer


arr = [1,2,3,4,8]
target = 6

# arr = [2,3,5,9]
# target = 10
print(solution(arr, target))
