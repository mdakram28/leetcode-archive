class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total = 0
        while mainTank:
            if mainTank >= 5 and additionalTank>0:
                mainTank -= 4
                additionalTank -= 1
                total += 5
            else:
                total += mainTank
                mainTank = 0
        return total*10