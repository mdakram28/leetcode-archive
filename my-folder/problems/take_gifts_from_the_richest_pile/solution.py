class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        for i in range(n):
            gifts[i] = -gifts[i]
        heapify(gifts)
        
        for _ in range(k):
            heappush(gifts, -math.floor(math.sqrt(-heappop(gifts))))
        
        return -sum(gifts)