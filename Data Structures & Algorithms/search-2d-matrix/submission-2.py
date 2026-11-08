from bisect import bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        first_col_numbers = [row[0] for row in matrix]
        candidate_row = bisect_right(first_col_numbers, target) - 1
        # target より大きいインデックスより1個小さいインデックスの行が対象になる
        
        # bisect_right が 0　を返した、つまり Target が [1,1] より小さいことになり必然的にFalse
        if candidate_row == -1:
            return False
        
        else:
            # 一致するものがあるとすれば bisect_right - 1
            # target がこの行の最初の数値より大きいことは保証されている
            # -1 してもインデックスがおかしくなることはない
            candidate_col = bisect_right(matrix[candidate_row], target) - 1

            if target == matrix[candidate_row][candidate_col]:
                return True
            else:
                return False
            
        
