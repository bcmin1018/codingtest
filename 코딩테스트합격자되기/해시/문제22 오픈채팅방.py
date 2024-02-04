def solution(record):
    dic = {}
    result = []
    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            dic[tmp[1]] = tmp[2]
        elif tmp[0] == "Change":
            dic[tmp[1]] = tmp[2]

    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            user = dic[tmp[1]]
            result.append(f'{user}님이 들어왔습니다.')
        elif tmp[0] == "Leave":
            user = dic[tmp[1]]
            result.append(f'{user}님이 나갔습니다.')
    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)