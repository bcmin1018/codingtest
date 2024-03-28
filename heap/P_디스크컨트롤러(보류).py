# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 각 작업의 요청은 순차적으로 들어오며 중복되지 않는다.
# 다음 작업을 할때 작업 시간을 고려해야한다.
#

# [작업이 요청되는 시점, 작업의 소요시간]
# [[0, 3], [2, 6], [1, 9]]
# 9
import heapq

def solution(jobs):
    n_jobs = sorted(jobs, key=lambda x:x[0])
    answer = 0
    start = -1
    now = 0
    for job in jobs:
        request, work = job[0], job[1]
        min_heap = []
        if start < request < now: # 작업 도중에 요청이 들어오면
            heapq.heappush(min_heap, (work, request))
        else: # 이미 전 작업이 완료 된 경우
            while min_heap:
                work_, request_ = heapq.heappop(min_heap)


            start = job[0]
            now = start + job[1]






    return n_jobs

jobs = [[0, 3], [2, 6], [1, 9]]

print(solution(jobs))