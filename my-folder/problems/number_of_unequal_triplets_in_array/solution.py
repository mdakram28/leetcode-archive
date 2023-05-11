class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        
        for n in nums:
            right[n] += 1
        
        count_r = len(right)
        
        total = 0
        for i, n in enumerate(nums):
            right[n] -= 1
            if right[n] == 0:
                count_r -= 1
            
            for l, lf in left.items():
                if l == n: continue
                total += lf*(len(nums)-i-1)
                # if right[l]:
                total -= lf*right[l]
                # if right[n]:
                total -= lf*right[n]
                # print(l, n, right, total)
            
            left[n] += 1
        
        return total