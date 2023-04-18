class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""

        for i in range(min(len(word1), len(word2))):
            answer = answer + word1[i] + word2[i]
        return answer + word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]