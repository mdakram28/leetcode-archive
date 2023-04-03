class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        freq = {}
        for num in nums:
            freq[num%value] = freq.get(num%value, 0) + 1
            
        if len(freq) == value:
            min_freq = min(freq.values())
            min_idx = len(nums)
            for n, f in freq.items():
                if f == min_freq and n < min_idx:
                    min_idx = n
        else:
            min_freq = 0
            min_idx = 0
            while min_idx < value:
                if min_idx not in freq:
                    break
                else:
                    min_idx += 1
                
        return min_freq*value + min_idx
            