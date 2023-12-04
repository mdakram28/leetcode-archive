from sortedcontainers import SortedList

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)

        sums = [0]*n
        q = SortedList()

        for i in sorted(range(n), key=lambda i: (nums[i]-i, i)):
            if nums[i] <= 0: continue

            qi = q.bisect_left(i)
            if qi == 0:
                sums[i] = nums[i]
            else:
                sums[i] = sums[q[qi-1]] + nums[i]

            while qi < len(q) and sums[q[qi]] <= sums[i]:
                q.pop(qi)
            
            # if qi == 0 or sums[i] > sums[q[qi-1]]:
            q.add(i)
            # print(i, q, sums)
        return max(sums[i] for i in q) if q else max(nums)


