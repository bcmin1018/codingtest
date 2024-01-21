def valid_check(x, y):
    return -5 <= x <=5 and -5 <= y <=5

def update_location(dir, x, y):
    if dir == 'U':
        x = x
        y = y+1
    elif dir == 'D':
        x = x
        y = y -1
    elif dir == 'R':
        x = x+1
        y = y
    elif dir == 'L':
        x = x -1
        y = y
    return x, y

def solution(dirs):
    x, y = 0, 0
    result = set()
    for dir in dirs:
        nx, ny = update_location(dir, x, y)
        if not valid_check(nx, ny):
            continue
        result.add((x, y, nx, ny))
        result.add((nx, ny, x, y))
        x, y = nx, ny
    return len(result)/2




