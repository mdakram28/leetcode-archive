class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        @cache
        def minLen(i, left, right):
            if i == len(words): return 0

            l = len(words[i])
            to_left = minLen(i+1, words[i][0], right)
            if words[i][-1] == left:
                to_left -= 1
            to_right = minLen(i+1, left, words[i][-1])
            if words[i][0] == right:
                to_right -= 1
            # print(f"{i=}, {left=}, {right=}, {to_left=}, {to_right=}")
            return l + min(to_left, to_right)
        
        return len(words[0]) + minLen(1, words[0][0], words[0][-1])