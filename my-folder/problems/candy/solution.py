class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cand = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                cand[i] = cand[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                cand[i] = max(cand[i], cand[i+1]+1)
        
        # print(cand)

        
        return sum(cand)
