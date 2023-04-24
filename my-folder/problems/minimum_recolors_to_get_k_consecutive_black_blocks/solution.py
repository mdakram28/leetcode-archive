class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = 0
        for i in range(k-1):
            if blocks[i] == 'W':
                w += 1
                
        min_w = float('inf')
        for i in range(k-1, n):
            if blocks[i] == 'W':
                w += 1
            min_w = min(min_w, w)
            if blocks[i-k+1] == 'W':
                w -= 1
        
        return min_w