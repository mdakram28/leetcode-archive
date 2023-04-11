class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m

        while l<r:
            mid = (l+r)//2
            if target > matrix[mid][-1]:
                l = mid+1
            else:
                r = mid
        
        row = l
        if row >= m:
            return False

        l = 0
        r = n
        while l<r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid+1
            else:
                r = mid
        col = l

        if col >= n:
            return False

        return matrix[row][col] == target
                