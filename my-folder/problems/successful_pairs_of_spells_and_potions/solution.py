class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ret = []
        for i in range(len(spells)):
            t = success/spells[i]
            l = 0
            r = len(potions)
            while l<r:
                mid = (l+r) // 2
                if potions[mid] < t:
                    l = mid+1
                else:
                    r = mid
            
            ret.append(len(potions)-l)
        return ret