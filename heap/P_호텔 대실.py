# 항상 끝나는 시간이 빠른 룸을 갖고 싶다면 힙 자료구조를 사용하면 된다.
import heapq
def convert_time(time):
    h, m = map(int, time.split(":"))
    return h*60 + m

def solution(book_time):
    n_book_time = []
    for b in book_time:
        n_book_time.append([convert_time(b[0]), convert_time(b[1])])

    n_book_time = sorted(n_book_time, key=lambda x:x[0])
    print(n_book_time)

    answer = 1
    min_heap = []
    for visitor in n_book_time:
        if len(min_heap) == 0:
            heapq.heappush(min_heap, visitor[1] + 10)
            continue
        if min_heap[0] > visitor[0]: #방이 차 있으면
            answer += 1
        else:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, visitor[1] + 10)
    return answer

book_time = [["5:00","15:00"],["10:00","20:00"],["20:30","23:00"],["15:30","23:30"]]
print(solution(book_time))