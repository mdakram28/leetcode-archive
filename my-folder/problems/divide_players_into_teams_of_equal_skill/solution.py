class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        team_total = sum(skill)/(n//2)
        if team_total != int(team_total): return -1
        team_total = int(team_total)
        
        f = defaultdict(int)
        for num in skill:
            f[num] += 2
    
        total = 0
        for num1 in skill:
            num2 = team_total - num1
            if f[num1] == 0 or f[num2] == 0:
                return -1
            total += num1*num2
            f[num2] -= 1
            f[num1] -= 1
        
        return total // 2