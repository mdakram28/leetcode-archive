class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = set(fronts)
        ans |= set(backs)
        for a, b in zip(fronts, backs):
            if a == b:
                ans.discard(a)
        
        return min(ans) if len(ans) > 0 else 0