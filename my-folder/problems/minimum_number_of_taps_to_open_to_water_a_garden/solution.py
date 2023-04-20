class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges = [(i-d, i+d) for i, d in enumerate(ranges)]
        ranges.sort()
        # print(ranges)

        max_end = 0
        i = 0
        count = 0
        while max_end < n and i <= n:
            new_max_end = max_end
            while i<=n and ranges[i][0] <= max_end:
                new_max_end = max(new_max_end, ranges[i][1])
                i += 1
            # print(i, new_max_end)
            if max_end == new_max_end:
                return -1
            max_end = new_max_end
            count += 1
            # print(f"{count=}, {max_end=}")
        
        return count

        