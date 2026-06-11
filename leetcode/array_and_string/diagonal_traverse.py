from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        w, h = len(mat[0]), len(mat)
        result = []
        col, row = 0, 0
        
        for _ in range(w * h):
            result.append(mat[row][col])
            
            if (row+col) % 2 == 0: # 짝수면
                if col == w -1: # 오른쪽 벽일때
                    row = row + 1
                elif row == 0: # 왼쪽 벽일때
                    col = col + 1
                else: # 벽이 아닐때
                    row = row - 1
                    col = col + 1

            else: # 홀수면
                if row == h - 1: # 아래 벽일때
                    col = col + 1
                elif col == 0: # 위 벽일때
                    row = row + 1
                else: # 벽이 아닐때
                    row = row + 1
                    col = col - 1
            
        return result