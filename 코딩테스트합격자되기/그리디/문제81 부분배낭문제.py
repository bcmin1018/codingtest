def solution(items, weight_limit):
    for item in items:
        item.append(item[1] / item[0])

    items.sort(key=lambda x: x[2], reverse=True)

    print(items)
    total_value = 0
    for item in items:
        if weight_limit > item[0]:
            total_value += item[1]
            weight_limit -= item[0]
        else:
            fraction = weight_limit / item[0]
            total_value += item[1] * fraction
            break

    print(total_value)


items = [[10, 19], [7, 10], [6, 10]]
weight_limit = 15

solution(items, weight_limit)

