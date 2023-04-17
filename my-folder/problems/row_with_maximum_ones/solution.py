class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_r = -1
        max_r_count = -1
        
        for r, row in enumerate(mat):
            count = row.count(1)
            if count > max_r_count:
                max_r_count = count
                max_r = r
        
        return max_r, max_r_count