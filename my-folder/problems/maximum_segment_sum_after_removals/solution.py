class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        acc = [0]
        # prefix sum
        for num in nums:
            acc.append(acc[-1] + num)
        
        # current max sum with boundries
        q = [(-sum(nums), 0, n - 1)]
        # removed index
        rm_idx = []
        
        
        ans = []
        for idx in removeQueries:
            bisect.insort(rm_idx, idx)
            while q:
                _, s, e = q[0]
                loc = bisect.bisect_left(rm_idx, s)
                idx = rm_idx[min(loc, len(rm_idx) - 1)]
                # if removed index fall between the boundry of largest sum
                if idx > e or idx < s: break
                heappop(q)
                if s < idx:
                    heappush(q, (-(acc[idx] - acc[s]), s, idx - 1))
                if e > idx:
                    heappush(q, (-(acc[e + 1] - acc[idx + 1]), idx + 1, e))
            if q:
                ans.append(-q[0][0])
            else:
                ans.append(0)
            
        
        return ans