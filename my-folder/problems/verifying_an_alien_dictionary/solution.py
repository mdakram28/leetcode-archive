class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}

        for i, c in enumerate(order):
            d[c] = i

        def is_in_order(w1, w2):
            i = 0
            l = min(len(w1), len(w2))
            while i<l and w1[i] == w2[i]:
                i += 1
            
            if i == l:
                return len(w1) <= len(w2)
            else:
                # print(f"{d[w1[i]]}, {d[w2[i]]}")
                return d[w1[i]] < d[w2[i]]
        
        for i in range(1, len(words)):
            if not is_in_order(words[i-1], words[i]):
                return False
        
        return True