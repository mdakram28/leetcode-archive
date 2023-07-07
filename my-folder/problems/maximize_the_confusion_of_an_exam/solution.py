class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def solution(char):
            num = 0
            start = 0
            ans = 0
            n = len(answerKey)
            for end, key in enumerate(answerKey):
                if key == char:
                    num += 1
                while num > k:
                    if answerKey[start] == char:
                        num -= 1
                    start += 1
                ans = max(ans, end-start+1)
            return ans

        return max(solution("T"), solution("F"))
