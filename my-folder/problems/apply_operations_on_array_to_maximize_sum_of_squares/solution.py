class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = defaultdict(int)
        
        for num in nums:
            for i, b in enumerate(reversed(bin(num))):
                if b=="1":
                    count[i] += 1
        
        total = 0
        for _ in range(k):
            num = 0
            for p in count.keys():
                if count[p]:
                    num |= 1<<p
                    count[p] -= 1
            total = (total + num*num)%(10**9 + 7)
        
        return total
        
        