class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            speed = (min_speed+max_speed) // 2
            hours = sum(math.ceil(p/speed) for p in piles)
            if hours <= h:
                max_speed = speed
            else:
                min_speed = speed+1
        
        return min_speed
            