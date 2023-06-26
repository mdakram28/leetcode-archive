from sortedcontainers import SortedList

class Solution:
    def totalCost(self, costs: List[int], k: int, cand: int) -> int:
        n = len(costs)

        INF = float('inf')
        left, right = [(INF, INF)], [(INF, INF)]
        l, r = 0, n-1

        while l<=r and l<cand:
            left.append((costs[l], l))
            l += 1
            if l<=r:
                right.append((costs[r], r))
                r -= 1

        heapify(left)
        heapify(right)

        ans = 0

        for ki in range(k):
            if left[0] < right[0]:
                ans += heappop(left)[0]
                if l<=r:
                    heappush(left, (costs[l], l))
                    l += 1
            else:
                ans += heappop(right)[0]
                if l<=r:
                    heappush(right, (costs[r], r))
                    r -= 1
        
        return ans

            

        