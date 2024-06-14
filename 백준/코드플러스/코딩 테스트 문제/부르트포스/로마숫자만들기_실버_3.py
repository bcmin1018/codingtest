# https://www.acmicpc.net/problem/16922
# N개의 자리에 중복으로 1, 5, 10, 50 을 넣을 수 있다.
# 1, 5, 10, 50 을 순차적으로 돌며 중복 순열을 적용하면 어떨까?
# N이 20까지 이므로 시간 복잡도가 최대 4 ^ 20 이므로 1,099,511,627,776..... 시간 초과가 날만하다.
# combinations_with_replacement 조합을 적용하니 성공했다. 조합과 순열의 차이는 알지만 순열이 느린 이유가 무엇일까?
# 사실 순서대로 나열할 필요가 없어 상대적으로 빠른 합을 사용하였다. 순열의 시간복잡도 n!, 중복 순열n^r, 조합 2^N 중복 조합


from itertools import combinations_with_replacement

N = int(input())
answer = []
for i in combinations_with_replacement([1, 5, 10, 50], N):
    answer.append(sum(i))
print(len(set(answer)))