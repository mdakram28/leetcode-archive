class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        w = defaultdict(int)
        total = 0
        for word in words:
            rev = word[1] + word[0]
            if w[rev]:
                w[rev] -= 1
                total += 4
            else:
                w[word]  += 1
            # print(word, w)
        for word, count in w.items():
            if count and word[0] == word[1]:
                total += 2
                break
        return total