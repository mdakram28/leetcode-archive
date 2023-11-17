class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(*sorted(zip(ages, scores))))[1]
        
        @cache
        def maxScore(i, minscore):
            if i >= len(players): return 0
            ans = 0
            for j in range(i, len(players)):
                if players[j] < minscore: continue
                ans = max(ans, players[j] + maxScore(j+1, players[j]))
            return ans
        
        return maxScore(0, 0)