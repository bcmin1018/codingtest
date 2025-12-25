#convert base-10 representation to base-7 representation
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = []
        minus = False
        if num == 0:
            return "0"
        else:
            if num < 0:
                minus = True
                num = -num
            while num > 0:
                fraction = num % 7
                result.append(str(fraction))
                num //= 7
            
        return "-" + "".join(result[::-1]) if minus else "".join(result[::-1])

num = -7
solution = Solution()
print(solution.convertToBase7(num))

        