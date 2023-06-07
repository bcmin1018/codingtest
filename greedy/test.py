# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
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