from collections import defaultdict

class Solution:
    ends = defaultdict(list)
    result = []
    def add_result(self, s, dots):
        start = 0
        ip = ''
        for end in dots:
            ip += s[start:end]
            ip += '.'
            start = end
        ip += s[dots[-1]:]
        self.result.append(ip)

    def recurse(self, s, dots, pos):
        if len(dots) == 3:
            if len(s) in self.ends[pos]:
                self.add_result(s, dots)
        else:
            for end in self.ends[pos]:
                dots.append(end)
                self.recurse(s, dots, end)
                dots.pop()



    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ends = defaultdict(list)
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                num = int(s[start:end])
                if num <= 255 and str(num) == s[start:end]:
                    self.ends[start].append(end)
                else:
                    break
        
        # print(self.ends)
        self.result = []
        self.recurse(s, [], 0)
        return self.result