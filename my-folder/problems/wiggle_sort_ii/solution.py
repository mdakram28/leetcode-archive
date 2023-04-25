class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return
        t = math.ceil(n/2)

        r = n-1
        l = 0
        while True:
            pval = nums[r]
            j = l
            for i in range(l, r):
                if nums[i] <= pval:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[r], nums[j] = nums[j], nums[r]
            if j > t:
                r = j-1
            elif j < t:
                l = j+1
            else:
                break
        
        mid_val = nums[t]
        pos = t-1
        for i in range(t-1, -1, -1):
            if nums[i] == mid_val:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos -= 1

        pos = t+1
        for i in range(t+1, n):
            if nums[i] == mid_val:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

        
        i = t-1
        j = n-1
        pos = 0

        for _ in range(n//2):
            nums[pos] |= (nums[i] << 16) & 0xFFFF0000
            pos += 1
            i -= 1
            nums[pos] |= (nums[j] << 16) & 0xFFFF0000
            pos += 1
            j -= 1

        if n%2:
            nums[pos] |= (nums[0] << 16) & 0xFFFF0000

        for i in range(n):
            nums[i] = nums[i]>>16







        