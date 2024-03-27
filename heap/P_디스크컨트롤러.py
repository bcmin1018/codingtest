# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 각 작업의 요청은 순차적으로 들어오며 중복되지 않는다.
# 같은 시간에 1, 2, 3, 4, 10 작업시간이 들어온 경우 작업 시간이 적은 걸 우선적으로 해결하면 1, 3, 6, 10, 20 평균 8,
# 작업 시간이 긴 걸 우선적으로 해결하면 10, 14, 17, 19, 20 평균이 높아진다.
# 시간을 1초씩 진행하며 해당 시간에 처리할 요청을 찾는다.
# 예를 들어 현재 시간이 3초 이면 3초에 작업이 요청되는 작업을 모두 찾는다. O(N)
# 찾은 작업을 모두 힙 자료구조에 넣어 작업의 소요시간이 작은 것이 루트 노드로 오도록 한다.


# [작업이 요청되는 시점, 작업의 소요시간]
# [[0, 3], [2, 6], [1, 9]]
# 9
import heapq

def solution(jobs):
    n_jobs = sorted(jobs, key=lambda x:x[0])
    answer = 0
    start = 0
    now = 0
    min_heap = []
    while True:
        for job in n_jobs:
            if start < job[0] == now:
                heapq.heappush(min_heap, (job[1], job[0]))

        if len(min_heap) > 0:
            current = heapq.heappop(min_heap)
            start = now
            now += current[0]
            answer += (now - current[1])





    return n_jobs

jobs = [[0, 3], [2, 6], [1, 9]]

print(solution(jobs))