class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        q = []
        it = iter(freq.items())
        for i in range(min(k,len(freq))):
            num, f = next(it)
            heappush(q, (f, num))

        for i in range(k, len(freq)):
            num, f = next(it)
            heappush(q, (f, num))
            heappop(q)
        
        return [num for f, num in q]
