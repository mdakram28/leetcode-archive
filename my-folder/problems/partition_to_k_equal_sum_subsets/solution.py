class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # Calculate subset sum
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum // k

        # If any value is more than the subset sum, we cannot have that in any set
        if any(val>subset_sum for val in nums):
            return False

        # Remove any number that is already subset sum
        nums = list(filter(lambda val: val!=subset_sum,nums))
        k = sum(nums)//subset_sum
        

        nums.sort()
        n = len(nums)
        not_taken = (1<<n) - 1
        
        @cache
        def can_partition(not_taken, k, curr_sum, i):
            '''
            not_taken : Bitmap - 1 represents available
            k : Number of remaining sets to make
            i : Index to check from
            curr_sum : Sum of numbers already taken by parent calls
            '''

            # The remaining values at the end will be exactly for 1 set
            if k <= 1: return True
            if i == n: return False
            
            # Otherwise if curr_sum is subset_sum, we got a set, find the next one
            if curr_sum == subset_sum: return can_partition(not_taken, k - 1, 0, 0)
            
            if not_taken&(1<<i) and curr_sum + nums[i] <= subset_sum:
                if can_partition(not_taken&(~(1<<i)), k, curr_sum+nums[i], i+1):
                    return True

            return can_partition(not_taken, k, curr_sum, i+1)
        
        return can_partition(not_taken, k, 0, 0)
