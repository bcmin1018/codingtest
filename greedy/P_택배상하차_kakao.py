def solution(cap, n, deliveries, pickups):
    answer = 0
    r_deliveries = deliveries[::-1] # 리스트를 반대로
    r_pickups = pickups[::-1]
    d, p = 0, 0
    for i in range(n): # 배달, 픽업해야할 수하물의 갯수를 카운트하여 계속 더한다.
        d += r_deliveries[i]
        p += r_pickups[i]
        while d>0 or p>0: # d, p가 0보다 크면 배달 또는 픽업해야하는 수하물이 있으므로 cap에서 마이너스하고 하차장을 갖다온 거리를 구한다. d, p가 0보다 작으면 아직 배달과 픽업을 더 할 수 있는 상태이므로 하차장을 갖다오지 않는다.
            d -= cap
            p -= cap
            answer += (n-i) * 2
    return answer

print(solution(4, 5, [1,0,3,1,10], [0,3,0,4,0]))