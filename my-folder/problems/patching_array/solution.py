class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.append(float('inf'))
        j = 0
        canmake = 0
        ans = 0
        while canmake < n:
            if nums[j] <= canmake+1:
                canmake += nums[j]
                j += 1
            else:
                # print(f"{canmake=} Adding {canmake+1}")
                canmake += canmake+1
                ans += 1
        
        return ans