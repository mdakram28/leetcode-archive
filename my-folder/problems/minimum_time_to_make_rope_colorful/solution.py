class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        max_t = neededTime[0]
        sum_t = max_t
        ret = 0
        l = 1
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                sum_t += neededTime[i]
                max_t = max(max_t, neededTime[i])
                l += 1
            else:
                if l>1:
                    ret += sum_t - max_t
                max_t = sum_t = neededTime[i]
                l = 1
        if l>1:
            ret += sum_t - max_t
        return ret
            
        

