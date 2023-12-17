class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        
        ans = float('inf')
        pref_total = list(accumulate(nums))
        pref_total.append(0)
        
        total = pref_total[-2]
        
        def get_cost(ind):
            # print(f"{pal=}")
            # ind = bisect_left(nums, pal)
            ans = ind*pal - pref_total[ind-1] + (total-pref_total[ind-1]) - (n-ind)*pal
            # print(ind, ind*pal - pref_total[ind-1], (total-pref_total[ind-1]) - (n-ind)*pal, ans)
            return ans
        
        j = 0
        for d in range(1, 10):
            dl = math.ceil(d/2)
            for i in range(10**(dl-1), 10**dl):
                if d%2 == 0:
                    pal = int(str(i) + str(i)[::-1])
                else:
                    pal = int(str(i) + str(i)[-2::-1])
                
                while j < n and nums[j] < pal:
                    j += 1
                # print(i, pal, j)
                ans = min(ans,get_cost(j))
                
                if j == n:
                    break
            else:
                continue
            break
            
            
        
        return ans
