class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        return all(mass+tot-ast >= ast for tot, ast in zip(accumulate(asteroids), asteroids))