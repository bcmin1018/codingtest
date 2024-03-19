import math

def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(0, len(progresses))]
    answer = []
    now = 0
    for i in range(1, len(days)):
        if days[i] > days[now]:
            answer.append(i-now)
            now = i
    answer.append(len(days)-now)
    return answer