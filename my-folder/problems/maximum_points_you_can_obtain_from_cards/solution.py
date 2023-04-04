class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 0
        total = 0
        while i < k:
            total += cardPoints[i]
            i += 1
        
        score = total
        i = 0
        while i < k:
            total -= cardPoints[k-i-1]
            total += cardPoints[-(i+1)]
            score = max(score, total)
            i += 1
        
        return score