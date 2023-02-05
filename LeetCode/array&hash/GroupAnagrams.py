strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 각 문자를 정렬한다.
# 알파벳이 같은 글자끼리 그룹화를 하는데 키는 공통 되고 정렬된 알파벳이다.

class Solution(object):
    def groupAnagrams(self, strs):

        sorted_dict = {}

        # 딕셔너리 만들기
        for str in strs:
            key = ''.join(sorted(str))
            sorted_dict[key] = []

        # 값을 넣기
        for str in strs:
            key = ''.join(sorted(str))
            sorted_dict[key].append(str)

        return sorted_dict.values()

if __name__ == "__main__":
    a = Solution()
    print(a.groupAnagrams(strs))


