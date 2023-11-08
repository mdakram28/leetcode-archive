class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = len(nums)
        rem = set(range(1, k+1))
        while len(rem) > 0:
            n = nums.pop()
            if n in rem:
                rem.remove(n)
            # print(n, rem, nums)
            
        return count - len(nums)