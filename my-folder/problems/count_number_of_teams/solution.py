from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        left = SortedList()
        right = SortedList(rating)
        
        total = 0
        for r in rating:
            right.remove(r)
            total += left.bisect_left(r) * (len(right) - right.bisect_right(r))
            left.add(r)
        
        
        left = SortedList()
        right = SortedList(rating[::-1])
        
        for r in rating[::-1]:
            right.remove(r)
            total += left.bisect_left(r) * (len(right) - right.bisect_right(r))
            left.add(r)
        
        return total