class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        i = 0
        i_max = len(nums)-2
        while i < i_max:
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            # print(f"{i= }, {target=}")

            while j < k:
                total = nums[j] + nums[k]
                # print(f"{j=}, {k=}, {total=}")
                if total < target:
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                elif total > target:
                    k -= 1
                    while nums[k] == nums[k+1] and j<k:
                        k -= 1
                else:
                    ret.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                    k -= 1
                    while nums[k] == nums[k+1] and j<k:
                        k -= 1

            i += 1
            while nums[i] == nums[i-1] and i<i_max:
                i += 1
        
        return ret