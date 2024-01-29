#

def solution(input):
    stack = []
    result = ""
    while input > 0:
        stack.append(input % 2)
        input = input // 2
    while stack:
        result += str(stack.pop())
    return result

input = 13
print(solution(input))

