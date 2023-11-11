class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, _ = moves.count("L"), moves.count("R"), moves.count("_")
        return max(
            _+l-r,
            _+r-l
        )