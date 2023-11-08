class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        total = 0
        for count in freq.values():
            if count == 1:
                return -1
            while count > 0 and count % 3 != 0:
                total += 1
                count -= 2
            total += count//3
        
        return total