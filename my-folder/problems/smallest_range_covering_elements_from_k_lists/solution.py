
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        cols = [0] * len(nums)

        min_heap = [(nums[r][0], r) for r in range(len(nums))]
        max_heap = [-nums[r][0] for r in range(len(nums))]
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        min_range = (float('inf'), 0)

        while True:
            min_val, min_row = heapq.heappop(min_heap)
            dist = -max_heap[0] - min_val
            
            if (dist, min_val) < min_range:
                min_range = (dist, min_val)

            cols[min_row] += 1
            if cols[min_row] == len(nums[min_row]):
                break
            heapq.heappush(min_heap, (nums[min_row][cols[min_row]], min_row))
            heapq.heappush(max_heap, -nums[min_row][cols[min_row]])

        return min_range[1], min_range[1]+min_range[0] 

