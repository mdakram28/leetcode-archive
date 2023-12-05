class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0: return -1

        if children == 1:
            if money == 3: return -1
            elif money == 7: return 1
            else: return 0

        count = 0
        for c in range(children-1):
            if money < 7:
                return count
            money -= 7
            count += 1
        
        if money == 7: return count+1
        elif money == 3: return count-1
        else: return count

        return count
        
