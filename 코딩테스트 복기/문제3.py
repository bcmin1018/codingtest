# 성적이 주어지고 결과 등수를 리턴하는 함수
# grade = [2,2,1] result = [1,1,3]
# grade = [3,2,1,2] result = [1,2,4,2]
# 제한사항 grade의 길이는 1 이상 1,000,000 이하
# grade의 각 원소는 1 이상 1,000,000,000 이하

import time
def solution(grade):
    result = []
    for g in grade:
        result.append(grade.index(g)+1)
    return result

# 두번쨰 방법 이중 for 문, 속도가 느리다.
def solution2(grade):
    result = []
    for i in range(0, len(grade)):
        rank = 1
        for j in range(0, len(grade)):
            if grade[i] < grade[j]:
                rank +=1
        result.append(rank)
    return result

# 최대 리스트의 길이가 100만이므로 100만 X 100만하면 답도 없다.이를 logN으로 해결해야한다.
def binary_search(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_[mid][0] == target:
            return list_[mid][1]
        elif list_[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

def solution3(grade):
    sorted_grade = []
    for i, g in enumerate(grade):
        sorted_grade.append((g, i+1))
    sorted_grade = sorted(sorted_grade)
    # print(sorted_grade)
    #[(1, 3), (2, 2), (2, 4), (3, 1)]
    result = []
    for g in grade:
        result.append(binary_search(sorted_grade, g))
    return result

# grade = [2,2,1]
grade = [3,2,1,2]
start = time.time()
print(solution3(grade))
print(time.time() - start)
