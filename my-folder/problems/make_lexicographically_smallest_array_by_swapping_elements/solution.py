class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        q = [(num, i) for i, num in enumerate(nums)]
        q.sort(reverse=True)
        ans = [0]*len(nums)
        
        while q:
            val, ind = q.pop()
            vals = [val]
            inds = [ind]
            
            while q and (q[-1][0] - vals[-1]) <= limit:
                val, ind = q.pop()
                vals.append(val)
                inds.append(ind)
            
            vals.sort()
            inds.sort()
            
            for val, ind in zip(vals, inds):
                ans[ind] = val
        
        return ans
        