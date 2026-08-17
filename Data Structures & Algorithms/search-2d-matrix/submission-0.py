class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        m = 0
        while l <= r:
            m = (r + l) // 2
            curr = matrix[m]
            if curr[0] == target or curr[-1] == target:
                return True
            if target >= curr[0] and target <= curr[-1]:
                break
            elif target < curr[-1]:
                r = m - 1
            else:
                l = m + 1
        if not(l<=r):
            return False
        left, right = 0, len(matrix[m])-1
        while left <= right:
            mid = (left+right) // 2
            
            if target > matrix[m][mid]:
                left = mid + 1
            elif target < matrix[m][mid]:
                right = mid - 1
            else:
                return True
        return False
