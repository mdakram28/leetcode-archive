class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        for num in nums:
            f[num] += 1
        heap = []
        for v, f in f.items():
            heappush(heap, (f, v))
            if len(heap) > k:
                heappop(heap)
        return [val for f, val in heap]