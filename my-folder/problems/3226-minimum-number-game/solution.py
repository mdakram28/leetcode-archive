class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        arr = []
        while nums:
            a = heappop(nums)
            b = heappop(nums)
            arr.append(b)
            arr.append(a)
        
        return arr
