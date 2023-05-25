from sortedcontainers import SortedList

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.append([float('inf'), float('inf')])
        intervals.sort(reverse=True, key=lambda x: x[0])
        
        sizes = [(float('inf'), float('inf'))]
        ans = {}

        for q in sorted(queries):
            while intervals[-1][0] <= q:
                start, end = intervals.pop()
                heappush(sizes, (end-start+1, end))
            while sizes[0][1] < q:
                heappop(sizes)
            ans[q] = sizes[0][0]
        
        return [ans[q] if ans[q]!=float('inf') else -1 for q in queries]