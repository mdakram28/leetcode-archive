class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        char_count = {
            char: [0]*len(words[0])
            for char in string.ascii_lowercase
        }
        mod = 10**9+7

        for word in words:
            for i, c in enumerate(word):
                char_count[c][i] += 1
        
        DP = [1]*(len(words[0])+1)
        DP[0] = 0
        prev = 1
        for i in range(len(target)):
            for j in range(1, len(words[0])+1):
                DP[j], prev = (char_count[target[i]][j-1]*prev + DP[j-1])%mod, DP[j]
            prev = 0
            # print(DP)

        return DP[-1]