class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            found = {nums[i]}
            count = 0
            for j in range(i+1, len(nums)):
                num = nums[j]
                p = num-1 in found
                n = num+1 in found
                if num in found:
                    pass
                elif p and n:
                    count -= 1
                elif p or n:
                    pass
                else:
                    count += 1
                found.add(num)
                ans += count
            # print(i, count)
        return ans