class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_idx = {}
        min_length = float('inf')
        for i, c in enumerate(cards):
            if c in last_idx:
                min_length = min(min_length, i - last_idx[c])
            last_idx[c] = i
        return min_length+1 if min_length != float('inf') else -1