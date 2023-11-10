class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        f = defaultdict(int)
        for num in nums:
            f[num] += 1
        
        vals = [-val for val in f.values()]
        heapify(vals)
        
        while len(vals) > 1:
            # print(vals)
            a = -heappop(vals)-1
            b = -heappop(vals)-1
            if a!=0:
                heappush(vals, -a)
            if b!=0:
                heappush(vals, -b)
        # print(vals)
        
        return 0 if len(vals) == 0 else -sum(vals)