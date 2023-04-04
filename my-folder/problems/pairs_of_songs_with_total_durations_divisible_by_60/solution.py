class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] %= 60
        
        f = collections.defaultdict(int)
        total = 0
        for t in time:
            total += f[(60-t)%60]
            f[t] += 1
        
        return total