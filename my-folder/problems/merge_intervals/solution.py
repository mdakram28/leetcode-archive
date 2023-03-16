class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0] + x[1])
        intervals.sort(key=lambda x: x[0])
        # print(f"{intervals=}")
        merged = []

        it = iter(intervals)
        [start, end] = next(it)
        # print(f"{start=}, {end=}")
        for interval in it:
            # print(f"{start=}, {end=}, {interval=}")
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start, end = interval
        # print(f"{start=}, {end=}")
        merged.append([start, end])
        return merged