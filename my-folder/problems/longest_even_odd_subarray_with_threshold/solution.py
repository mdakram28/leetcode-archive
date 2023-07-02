class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        prev = nums[0]
        curr_len = 1 if nums[0]%2 == 0 and nums[0] <= threshold else 0
        ans = curr_len
        for curr in nums[1:]:
            if curr > threshold:
                curr_len = 0
            else:
                if prev % 2 == curr % 2:
                    curr_len = 1 if curr%2 == 0 else 0
                elif curr_len > 0 or curr%2 == 0:
                    curr_len += 1
            # print(curr_len)
            if curr_len > ans:
                ans = curr_len
            prev = curr
        return ans