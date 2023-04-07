class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        start = 0
        end = 0
        max_q = deque()
        ret = []
        
        while end < k:
            n = nums[end]
            while max_q and max_q[-1][0] <= n:
                max_q.pop()
            max_q.append((n, end))
            end += 1

        ret.append(max_q[0][0])

        while end < len(nums):
            if max_q[0][1] == start:
                max_q.popleft()
            start += 1

            n = nums[end]
            while max_q and max_q[-1][0] <= n:
                max_q.pop()
            max_q.append((n, end))
            ret.append(max_q[0][0])
            end += 1
        
        return ret