def binarySearch(arr, val):
    start = 0
    end = len(arr)
    while start < end:
        mid = start + (end - start) // 2
        if val <= arr[mid][0]:
            start = mid + 1
        else:
            end = mid
 
    return start-1

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        q = defaultdict(list)
        for i, (a,b) in enumerate(queries):
            a,b = min(a,b), max(a,b)
            q[b].append((a, i))
        
        ans = [-1]*len(queries)
        # (h,i)
        st = []
        for j in range(len(heights)-1, -1, -1):
            h = heights[j]
            while st and st[-1][0] <= h:
                st.pop()
            st.append((h, j))
            
            if j not in q: continue
                
            for a, qi in q[j]:
                if a==j or heights[a] < heights[j]:
                    ans[qi] = j
                else:
                    pos = binarySearch(st, max(heights[j], heights[a])+1)
                    ans[qi] = -1 if pos == -1 else st[pos][1]
        
        return ans