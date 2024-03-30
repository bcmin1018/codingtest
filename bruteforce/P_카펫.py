def solution(brown, yellow):
    answer = []
    size = brown + yellow
    w = 1
    while True:
        h = size // w
        if (w-2)*(h-2) == yellow and w * h == size and w >=h:
            answer.append(w)
            answer.append(h)
            break
        w += 1
    return answer