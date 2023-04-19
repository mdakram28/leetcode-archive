class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)
        if n == 1:
            return 0
        bucket_size = math.ceil((max_val-min_val)/(n-1))
        if bucket_size == 0:
            return 0
        INF = float('inf')
        bucket_min = [INF] * n
        bucket_max = [-INF] * n

        for num in nums:
            b = (num-min_val)//bucket_size
            bucket_min[b] = min(bucket_min[b], num)
            bucket_max[b] = max(bucket_max[b], num)
        
        prev_val = bucket_max[0]
        i = 1
        while i<n and prev_val == -INF:
            prev_val = bucket_max[i]
            i += 1
        
        max_diff = -INF
        while i<n:
            if bucket_min[i] == INF:
                i += 1
                continue
            max_diff = max(max_diff, bucket_min[i]-prev_val)
            prev_val = bucket_max[i]
            i+=1
        
        return max_diff if max_diff!=-INF else 0