class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        total = 0
        for i in range(len(words)):
            a = ''.join(reversed(list(words[i])))
            for j in range(i+1, len(words)):
                if a == words[j]:
                    total += 1
                    break
        return total