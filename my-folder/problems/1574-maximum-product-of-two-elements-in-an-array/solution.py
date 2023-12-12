class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2: 
            return (nums[0]-1)*(nums[1]-1)
        
        n0, i0 = min((n, i) for i, n in enumerate(nums))
        n1, i1 = min((n, i) for i, n in enumerate(nums) if i != i0)

        _n0, _i0 = max((n, i) for i, n in enumerate(nums))
        _n1, _i1 = max((n, i) for i, n in enumerate(nums) if i != _i0)
        
        return max(
            (n0-1)*(n1-1),
            (_n0-1)*(_n1-1)
        )
