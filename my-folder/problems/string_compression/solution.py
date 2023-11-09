class Solution:
    def compress(self, chars: List[str]) -> int:
        end = 0

        prev = chars[0]
        count = 0
        for c in chars:
            if c == prev:
                count += 1
                continue
            
            chars[end] = prev
            end += 1
            if count > 1:
                for d in str(count):
                    chars[end] = d
                    end += 1

            count = 1
            prev = c
        
        
        chars[end] = prev
        end += 1
        if count > 1:
            for d in str(count):
                chars[end] = d
                end += 1
        
        while len(chars) > end:
            chars.pop()