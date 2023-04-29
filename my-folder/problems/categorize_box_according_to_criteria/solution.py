class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        v = length * width * height
        bulky = v >= 10**9 or max(length, width, height) >= 10000
        heavy = mass >= 100
        
        cat = {
            (False, False): "Neither",
            (False, True): "Heavy",
            (True, False): "Bulky",
            (True, True): "Both"
        }
        return cat[(bulky, heavy)]