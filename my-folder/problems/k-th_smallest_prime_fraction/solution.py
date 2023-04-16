from fractions import Fraction

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        
        heap = [(arr[r]/arr[n-1], r, n-1) for r in range(n)]
        heapq.heapify(heap)

        for _ in range(k-1):
            val, r, c = heapq.heappop(heap)
            if c :
                heapq.heappush(heap, (arr[r]/arr[c-1], r, c-1))

        return arr[heap[0][1]], arr[heap[0][2]]

        

        