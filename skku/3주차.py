# import random
# db = random.sample(range(10000), 1000)
# key = db[109]
# print(db.index(key))

# 검색
# 1. 순차 검색
# 앞에서 부터 하나씩 검색
# def seq_search_ox(s, key):
#     if len(s) != 0:
#         if s[0] == key:
#             return True
#         else:
#             seq_search_ox(s[1:], key)
#     else:
#         return False
#
# print(seq_search_ox([3,5,4,2], 4))
#
# def seq_search_ox2(s, key):
#     while len(s) != 0:
#         if s[0] == key:
#             return True
#         else:
#             s = s[1:]
#     return False
#
# print(seq_search_ox2([3,5,4,2], 4))


# 순차 검색의 단점은 키가 맨뒤에 있거나 없는 경우에 전체 리스트를 다 검색하는 비효율성이다.


# 2. 이분 검색 (바이너리 서치)
# 리스트는 정렬이 되어야 한다.
# 리스트의 중간 위치를 찾고 중간보다 큰지 작은지를 비교하는 형식을 반복해서 실행

def bin_search_ox(ss, key):
    if len(ss) != 0:
        mid = len(ss) // 2
        if key > ss[mid]:
            bin_search_ox(ss[mid:], key)
        elif key < ss[mid]:
            bin_search_ox(ss[:mid-1], key)
        else:
            True

    else:
         return False

def bin_search_ox2(ss, key):
    while len(ss) !=0:
        mid = len(ss) // 2
        if ss[mid] == key:
            return True
        elif ss[mid] < key:
            ss = ss[:mid]
        else:
            ss = ss[mid+1:]


# 정렬된 경우에는 이분 검색의 검색 횟수가 적을 수 있다.
# 무조건 적으로 이분 탐색이 성능이 좋은 것은 아니다. 찾는 값이 리스트의 앞부분에 있으면 이분 탐색의 성능은 줄어들 수 있다.


# 찾는 위치 알려주기
# 찾으면 인덱스를 리턴
# 인덱스 위치를 나타내는 count가 필요함

def seq_search(s, key):
    i = 0
    for x in s: # 리스의 요소를 하나씩 꺼낸다.
        if x ==key: # 키와 비교 하여 동일하면 인덱스를 반환
            return i
        i += 1  # 그렇지 않으면 인덱스를 하나 씩 올린다.
    return None

print(seq_search([3,5,2,1], 2))

# 이분 검색은 low high 변수를 사용한다.
def bin_search(ss, key):
    low = 0
    high = len(ss) -1
    while low <= high:
        mid = (high + low) //2
        if key == ss[mid]:
            return mid
        elif key < ss[mid]:
            high = mid -1 # key가 중앙보다 작으면 high 를 중앙-1 값으로 변경해야한다.
        else:
            low = mid + 1


