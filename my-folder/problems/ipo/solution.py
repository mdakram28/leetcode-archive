class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        min_heap = [t for t in zip(capital, profits)]
        heapq.heapify(min_heap)

        # print(min_heap)
        while (min_heap or max_heap) and k:
            while min_heap and w >= min_heap[0][0]:
                profit = heapq.heappop(min_heap)[1]
                heapq.heappush(max_heap, -profit)
            # print(max_heap)
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
            k -= 1

        return w