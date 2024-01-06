class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums:
            xor ^= num
        
        return bin(xor).count("1")