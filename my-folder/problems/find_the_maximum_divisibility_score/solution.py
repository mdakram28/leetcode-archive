class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # divisors.sort()
        min_count = float('inf')
        min_count_d = divisors[0]
        for d in divisors:
            count = 0
            for n in nums:
                if n%d:
                    count += 1
                if count > min_count:
                    break
            else:
                if count < min_count:
                    min_count = count
                    min_count_d = d
                elif count == min_count:
                    min_count_d = min(min_count_d, d)
            # print(d, count, min_count)
        
        return min_count_d