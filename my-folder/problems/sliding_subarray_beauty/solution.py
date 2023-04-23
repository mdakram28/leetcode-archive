class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = defaultdict(int)
        ans = []
        
        for num in nums[:k-1]:
            freq[num] += 1
        
        for i in range(k-1, len(nums)):
            freq[nums[i]] += 1
            
            total = 0
            for j in range(-50, 0):
                total += freq[j]
                if total >= x:
                    ans.append(j)
                    break
            else:
                ans.append(0)
            
            freq[nums[i-k+1]] -= 1
        
        return ans