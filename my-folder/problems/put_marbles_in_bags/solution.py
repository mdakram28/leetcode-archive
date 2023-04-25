class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
            
        
        n = len(weights)
        
        
        for i in range(n-1):
            weights[i] += weights[i+1]
        weights.pop()
        
        weights.sort()
        return sum(weights[1-k:]) - sum(weights[:k-1])