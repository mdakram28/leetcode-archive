def add_nums(nums, node):
    match = 0
    for num in nums:
        if num in node:
            match += 1
            node = node[num]
        else:
            node[num] = {}
            node = node[num]
    return match

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        end = 0
        n = len(nums)
        div = 0
        count = 0
        root = {}
        for start in range(n):
            while end<n and (div < k or nums[end]%p != 0):
                if nums[end]%p == 0: div += 1
                end += 1
            m_len = add_nums(nums[start:end], root)
            # print(nums[start:end], m_len, root)
            count += end-start - m_len
            if nums[start]%p == 0: div -= 1
            start += 1
        return count
            
            