# https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    # 아스키코드 65 ~ 90
    # 77 보다 크면 조이스틱 아래로

    target = [ord(w) for w in name]  # ex) [77, 66, 88]
    start = [ord('A')] * len(name)  # ex) [65, 65, 65]
    count = 0

    for i in range(0, len(target)):
        if (target[i] == start[i]):  # A
            count += 1
            continue

        elif (target[i] > start[i]):
            if (target[i] - start[i] > 12):
                count += 25 - (target[i] - start[i]) + 1
            else:
                count += target[i] - start[i]
                count += 1

        elif (target[i] < start[i]):
            count += start[i] - target[i]
            count += 1

    answer = count
    return answer