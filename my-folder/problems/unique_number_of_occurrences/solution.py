class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = [False] * (len(arr)+1)
        for num in Counter(arr).values():
            if seen[num]:
                return False
            seen[num] = True
        
        return True