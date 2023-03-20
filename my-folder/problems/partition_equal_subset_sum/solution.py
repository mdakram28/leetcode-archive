class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targets = set([0])
        temp = []
        for n in nums:
            temp.clear()
            for t in targets:
                if (n + t) not in targets:
                    temp.append(n+t)
            targets.update(temp)
        return (sum(nums)/2) in targets
                