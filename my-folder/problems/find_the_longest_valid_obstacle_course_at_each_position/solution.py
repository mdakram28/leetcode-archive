from sortedcontainers import SortedList

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # lens = defaultdict(int)
        ends = SortedList([0])
        for i, num in enumerate(obstacles):
            obstacles[i] = new_len = ends.bisect_right(num)
            if new_len == len(ends):
                ends.add(num)
            else:
                if num < ends[new_len]:
                    del ends[new_len]
                    ends.add(num)
        return obstacles