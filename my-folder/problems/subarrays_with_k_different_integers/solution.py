class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        start = 0
        max_end = 0
        min_end = 0

        n = len(nums)
        ret = 0
        
        f_min = collections.defaultdict(int)
        f_max = collections.defaultdict(int)
        uniq = 0

        for start in range(n):

            while min_end < n and uniq < k:
                if f_min[nums[min_end]] == 0:
                    uniq += 1
                f_min[nums[min_end]] += 1
                min_end += 1
            
            while max_end < n and f_min[nums[max_end]]:
                f_max[nums[max_end]] += 1
                max_end += 1
            
            if uniq != k:
                break

            ret += max_end - min_end + 1
            # print(nums[start:min_end], nums[start:max_end])

            f_min[nums[start]] -= 1
            f_max[nums[start]] -= 1
            if f_min[nums[start]] == 0:
                uniq -= 1
        
        return ret

            



