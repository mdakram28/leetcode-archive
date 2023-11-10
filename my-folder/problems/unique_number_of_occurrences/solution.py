class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = defaultdict(int)
        for num in arr:
            f[num] += 1
        return len(set(f.values())) == len(f)