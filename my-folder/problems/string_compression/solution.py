class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        start = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                continue
            
            chars[j] = chars[start]

            if (i-start) > 1:
                num = str(i-start)
                for j, d in zip(range(j+1, 20000), num):
                    chars[j] = d
            
            j += 1
            start = i
        
        
        chars[j] = chars[start]

        if (len(chars)-start) > 1:
            num = str(len(chars)-start)
            for j, d in zip(range(j+1, 20000), num):
                chars[j] = d
        
        j += 1
        return j