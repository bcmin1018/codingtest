# 시간 복잡도는 리스트를 순회 하므로 O(N) 이고 append와 pop은 O(1)

def solution(inputs):
    stack = []
    for input in inputs:
        if input == '(':
            stack.append(input)
        elif input == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True


# inputs = '(())()'
inputs = ')()('
print(solution(inputs))