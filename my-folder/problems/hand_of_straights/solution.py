class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        f = defaultdict(int)
        hand.sort()
        for h in hand:
            f[h] += 1
        
        for num in hand:
            if f[num] == 0: continue
            for i in range(num, num+groupSize):
                if f[i] == 0: return False
                f[i] -= 1
        
        return True