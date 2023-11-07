class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        
        for num in nums:
            for i, b in enumerate(reversed(bin(num))):
                if b == '1':
                    count[i] += 1
        
        # print(count)
        
        num = 0
        for pos, c in count.items():
            if c >= k:
                num |= 1 << pos
        
        return num