class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for r in range(n)]

        top = 0
        bottom = n-1
        left = 0
        right = n-1

        i = 1
        while i<n*n:
            
            r = top
            for c in range(left, right):
                ans[r][c] = i
                i += 1
            
            c = right
            for r in range(top, bottom):
                ans[r][c] = i
                i += 1
            
            r = bottom
            for c in range(right, left, -1):
                ans[r][c] = i
                i += 1
            
            c = left
            for r in range(bottom, top, -1):
                ans[r][c] = i
                i += 1
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1 

        if n%2:
            ans[n//2][n//2] = n*n
        return ans