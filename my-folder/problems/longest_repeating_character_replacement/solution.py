from string import ascii_uppercase

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_diff = 1
        for c in set(s):
            rem = k
            start = -1
            for end in range(len(s)):
                if s[end] == c:
                    pass
                else:
                    if rem > 0:
                        rem -= 1
                    else:
                        # Free 1 char
                        while rem == 0:
                            start += 1
                            if s[start] != c:
                                rem += 1
                        rem -= 1
                # print(f"{start=}, {end=}")
                max_diff = max(max_diff, end-start)
        
        return max_diff