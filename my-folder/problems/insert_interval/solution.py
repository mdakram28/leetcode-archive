class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i in intervals:
            if newInterval is None or i[1] < newInterval[0]:
                merged.append(i)
            elif i[0] > newInterval[1]:
                if newInterval is not None:
                    merged.append(newInterval)
                    newInterval = None
                merged.append(i)
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        
        if newInterval is not None:
            merged.append(newInterval)
            newInterval = None
        return merged