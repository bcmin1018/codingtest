import math


def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(0, len(progresses))]
    answer = []
    days.append(1000)

    cnt = 1
    for i in range(0, len(days) - 1):
        if days[i + 1] <= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    return answer