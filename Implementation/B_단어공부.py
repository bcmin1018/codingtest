#시간 복잡도 해시 테이블을 만들고 카운트를 위해 순회 2 * O(N), 정렬 O(N), 순회하면서 중복된 값이 있는지 확인 O(N)

# words = str(input())
# unique_words = set(words.upper())
# hash_table = {word: 0 for word in unique_words}
#
# for w in words:
#     hash_table[w.upper()] += 1
#
# sorted_hash_table = sorted(hash_table.items(), key=lambda x:x[1], reverse=True)
#
# # 가장 많이 사용된 알파벳 중에서 중복된 값이 있는지 체크
# duplicate_check = False
# tmp = 0
# for w in sorted_hash_table:
#     if w[1] > tmp:
#         tmp = w[1]
#     elif w[1] == tmp:
#         duplicate_check = True
#
# if not duplicate_check:
#     print(sorted_hash_table[0][0])
# else:
#     print("?")

words = input().upper() # 알파벳 리스트
set_words = list(set(words)) # 중복되지 않은 알파벳 리스트

# 고유한 알파벳의 개수
cnt = []
for w in set_words:
    cnt.append(words.count(w))

# 고유한 알파벳 개수가 같으면 ? 출력
if cnt.count(max(cnt)) > 1:
    print("?")
else: # 그렇지 않으면 인덱스를 통해 알파벳 찾기
    print(set_words[(cnt.index(max(cnt)))])





