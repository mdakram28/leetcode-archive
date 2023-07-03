class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False

        delta = []

        for a, b in zip(s, goal):
            if a!=b:
                if len(delta) == 2: return False
                delta.append((a, b))
        
        if len(delta) == 1: return False
        if len(delta) == 0: return len(set(s)) != len(s)

        # print(delta)

        a1, b1 = delta[0]
        a2, b2 = delta[1]
        return a1 == b2 and a2 == b1