MAPPING = [
    [],
    [],
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
    ['j','k','l'],
    ['m','n','o'],
    ['p','q','r', 's'],
    ['t','u','v'],
    ['w','x','y','z']
]
class Solution:
    result = []
    digits = ''
    def addLetters(self, prefix, pos):
        if pos == len(self.digits):
            self.result.append(prefix)
        else:
            for c in MAPPING[int(self.digits[pos])]:
                self.addLetters(prefix + c, pos+1)

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.result = []
        if digits == '':
            return []
        self.addLetters('', 0)
        return self.result