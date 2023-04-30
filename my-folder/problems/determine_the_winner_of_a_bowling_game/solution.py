class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        last10 = -5
        
        score1 = sum(player1)
        for i in range(len(player1)):
            if i-last10 <= 2: score1 += player1[i]
            if player1[i] == 10:
                last10 = i
        
        last10 = -5
        score2 = sum(player2)
        for i in range(len(player2)):
            if i-last10 <= 2: score2 += player2[i]
            if player2[i] == 10:
                last10 = i
        
        if score1 == score2: return 0
        elif score1 > score2: return 1
        else: return 2