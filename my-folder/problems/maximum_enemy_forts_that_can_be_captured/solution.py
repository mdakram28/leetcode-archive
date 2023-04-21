class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
        last_i = -1
        last_val = 0
        max_forts = 0
        for i, num in enumerate(forts):
            if num:
                if last_val*num == -1:
                    max_forts = max(max_forts, i-last_i)
                last_i = i
                last_val = num
        
        return max(max_forts-1, 0)
                