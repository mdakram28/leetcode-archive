class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        nums = [ord(c)-ord('a') for c in s]
        
        # for i in range(n-1, -1, -1):
        i = n-1
        # while i >= 0:
        
        invalid = False
        
        def inc(i):
            nonlocal invalid
            if i < 0:
                invalid = True
                return
            
            nums[i] += 1
            if nums[i] == k:
                nums[i] = 0
                inc(i-1)
            if i > 0 and nums[i] == nums[i-1]:
                inc(i)
            if i > 1 and nums[i] == nums[i-2]:
                inc(i)
        
        inc(n-1)
        
        if invalid:
            return ""
        return ''.join(chr(ord('a') + num) for num in nums)