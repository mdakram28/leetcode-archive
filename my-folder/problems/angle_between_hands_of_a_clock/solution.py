class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a_m = minutes*360/60
        a_h = (hour + minutes/60)*360/12

        diff = abs(a_m-a_h)
        return min(diff, 360-diff)