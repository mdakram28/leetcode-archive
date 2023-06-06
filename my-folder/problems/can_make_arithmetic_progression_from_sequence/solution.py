class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mn = min(arr)
        mx = max(arr)

        if (mx-mn)%(len(arr)-1) != 0: return False
        d = (mx-mn)//(len(arr)-1)
        if d == 0: return True

        slots = [False] * (mx-mn+1)

        for num in arr:
            if (num-mn)%d != 0 or slots[num-mn]: return False
            slots[num-mn] = True
            
        return True