def solution(strings, n):
    # return sorted(strings, key=lambda x : x[n])
    return sorted(strings, key=lambda x: (x[n], x))

strings = ["sun", "bed", "car"]
print(solution(strings, 1))