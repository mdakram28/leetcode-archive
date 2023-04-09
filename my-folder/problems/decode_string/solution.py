class Solution:
    def decodeString(self, s: str) -> str:
        ret = []
        i = 0
        
        def decode_add(rep, pref):
            nonlocal i
            # print(pref, rep, i, ''.join(ret))
            rep_start = len(ret)
            while i < len(s) and s[i]!=']':
                if s[i].isdigit():
                    dig_start = i
                    while s[i] != '[':
                        i += 1
                    i += 1
                    decode_add(int(s[dig_start:i-1]), pref+"\t")
                else:
                    ret.append(s[i])
                    i += 1
            i += 1
            # print(pref, rep, i, ''.join(ret[rep_start:]*rep))
            ret.extend(ret[rep_start:]*(rep-1))
        
        decode_add(1, "")
        return ''.join(ret)