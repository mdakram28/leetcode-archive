class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        l = 0
        heap = []
        i = 1
        n = len(heights)

        while i < n and len(heap) < ladders:
            if heights[i] > heights[i-1]:
                # print(f"{heights[i]-heights[i-1]}")
                heapq.heappush(heap, heights[i]-heights[i-1])
            i += 1

        if len(heap) != ladders:
            return n-1

        while i<n:
            if heights[i] > heights[i-1]:
                heapq.heappush(heap, heights[i]-heights[i-1])
                l += heapq.heappop(heap)
                if l > bricks:
                    break
                # print(f"{heights[i]-heights[i-1]}, {l=}")

            i += 1
        
        return i-1