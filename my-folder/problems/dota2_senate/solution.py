from sortedcontainers import SortedList
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        can_vote = [True] * n

        i, j = 0, 0
        curr = 0
        remR, remD = senate.count("R"), senate.count("D")
        if remR == 0: return "Dire"
        elif remD == 0: return "Radiant"

        while not can_vote[i] or senate[i] != 'R':
            i = (i+1)%n
        while not can_vote[j] or senate[j] != 'D':
            j = (j+1)%n
        

        while remR and remD:
            # print(i, j, curr, remR, remD)
            if curr == i:
                can_vote[j] = False
                remD -= 1
                if remD == 0: break
            else:
                can_vote[i] = False
                remR -= 1
                if remR == 0: break

            j = (j+1)%n
            while not can_vote[j] or senate[j] != 'D':
                j = (j+1)%n

            i = (i+1)%n
            while not can_vote[i] or senate[i] != 'R':
                i = (i+1)%n

            curr = (curr+1)%n
            while not can_vote[curr]:
                curr = (curr+1)%n

        
        return "Radiant" if remR else "Dire"