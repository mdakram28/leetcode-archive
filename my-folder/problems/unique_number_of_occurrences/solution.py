class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        found = set()
        for f in count.values():
            if f in found: return False
            found.add(f)
        return True