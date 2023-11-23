class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        ans = []
        for l, r in zip(left, right):
            subnums = nums[l:r+1]
            subnums.sort()
            diff = subnums[1]-subnums[0]
            for i in range(1, len(subnums)):
                if subnums[i]-subnums[i-1] != diff:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        
        return ans