from sortedcontainers import SortedList
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            i = bisect_left(ans, num)
            if i == len(ans):
                ans.append(num)
            else:
                ans[i] = num
        return len(ans)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.lengthOfLIS(map(itemgetter(1), envelopes))
        
        