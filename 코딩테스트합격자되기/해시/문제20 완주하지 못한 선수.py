# 시간 복잡도는 N, N-1의 리스트를 순차로 순회하여 O(N), O(N-1) 를 더하면 O(2N-1)이므로 O(N)이다.
def solution(participant, completion):

    dic = {}
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    for c in completion:
        if c in dic:
            dic[c] -=1

    for k in dic.keys():
        if dic[k] >0:
            return k


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
print(solution(p, c))