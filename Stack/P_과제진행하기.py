def end_time_cal(s_time, w_time):
    hh, mm = map(int, s_time.split(":"))
    n_hh = ((mm+int(w_time)) // 60) + hh
    n_mm = (mm+int(w_time)) % 60
    return str(n_hh) + ":" + str(n_mm)

# def solution(plans):
#     sorted_plans = sorted(plans, key=lambda x: x[1])
#     print(sorted_plans)
#
# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
# print(solution(plans))

print(end_time_cal("12:30", "40"))


def end_time_cal(s_time, w_time):
    hh, mm = map(int, s_time.split(":"))
    n_hh = ((mm + int(w_time)) // 60) + hh
    n_mm = (mm + int(w_time)) % 60
    return str(n_hh) + ":" + str(n_mm)


def solution(plans):
    sorted_plans = sorted(plans, key=lambda x: x[1])
    for p in sorted_plans:
        p.append(end_time_cal(p[1], p[2]))

    stack = []