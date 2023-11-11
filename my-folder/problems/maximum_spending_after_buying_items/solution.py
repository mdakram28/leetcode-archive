class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        d = 1
        q = [(row.pop(), r) for r, row in enumerate(values)]
        heapify(q)
        
        total = 0
        while q:
            minval, r = heappop(q)
            total += d*minval
            d += 1
            if len(values[r]) > 0:
                heappush(q, (values[r].pop(), r))
        
        return total
            