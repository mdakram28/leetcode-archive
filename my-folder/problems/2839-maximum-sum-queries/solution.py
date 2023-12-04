from sortedcontainers import SortedList

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        sl = SortedList()
        height = defaultdict(int)

        def add_height(x, h):
            # print(f"adding {h=} at {x=}")
            hi = sl.bisect_left(x)
            while hi > 0 and height[sl[hi-1]] <= h:
                sl.pop(hi-1)
                hi -= 1

            if hi == len(sl):
                sl.add(x)
                height[x] = h
            elif height[sl[hi]] < h:
                sl.add(x)
                height[x] = h
            # print(sl)
        
        def get_height(x):
            hi = sl.bisect_left(x)
            ret = height[sl[hi]] if hi < len(sl) else -1
            # print(f"getting height at {x=}, {hi=}, {ret=}")
            return ret
        

        ans = [-1]*len(queries)
        q = list(zip(nums1, nums2))
        q.sort()

        for qi, (miny, minx) in sorted(enumerate(queries), key=lambda item: -item[1][0]):
            # print(qi, (miny, minx))
            while q and q[-1][0] >= miny:
                add_height(q[-1][1], q[-1][0] + q[-1][1])
                q.pop()
            ans[qi] = get_height(minx)
        
        return ans
        
            
        
