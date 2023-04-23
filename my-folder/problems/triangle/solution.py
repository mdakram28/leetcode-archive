class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        
        @cache
        def min_sum(r, c):
            if r == rows: return 0
            return triangle[r][c] + min(min_sum(r+1, c), min_sum(r+1, c+1))
        
        return min_sum(0, 0)