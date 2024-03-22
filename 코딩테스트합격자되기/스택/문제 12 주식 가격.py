#https://school.programmers.co.kr/learn/courses/30/lessons/42584

# def solution(prices):
#     answer = []
#     for i in range(0, len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             if prices[j] < prices[i]:
#                 cnt+=1
#                 break
#             cnt+=1
#         answer.append(cnt)
#     return answer

def solution(prices):
    answer = []
    stack = []
    for i in range(0, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer.append(i - j)
        stack.append(i)

    print(answer)
    print(stack)
    while stack:
        j = stack.pop()
        answer.append(j - stack[-1])
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))