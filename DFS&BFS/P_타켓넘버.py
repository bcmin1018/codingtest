def solution(numbers, target):
    answer = []
    def dfs(i, sum_):
        if i == len(numbers):
            if sum_ == target:
                answer.append(sum_)
            return
        else:
            dfs(i + 1, sum_ + numbers[i])
            dfs(i + 1, sum_ - numbers[i])

    dfs(0, 0)
    return len(answer)

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))