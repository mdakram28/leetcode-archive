class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = Deque()
        max_l = 0
        q.append(-1)
        k+=1

        for i, num in enumerate(nums):
            if num == 0:
                q.append(i)
            if len(q) > k:
                q.popleft()
            max_l = max(max_l, i-q[0])
        
        return max_l