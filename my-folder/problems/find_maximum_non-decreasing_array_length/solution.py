class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        ans = 1
        
        T = list(accumulate(nums))
        F = [(0, -1)]
        D = []
        
        for i, t in enumerate(T):
            j = F[bisect_right(F, (t, float('inf')))-1][1]
            if j >= 0:
                f = t+t-T[j]
                D.append(1 + D[j])
            else:
                f = t+t
                D.append(1)
                
            # print(F, f, i, t, j)
            while F and F[-1][0] >= f:
                F.pop()
            F.append((f, i))
            
        # print(D)
        # print(F)
        return D[-1]