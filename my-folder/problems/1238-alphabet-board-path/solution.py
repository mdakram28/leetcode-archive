class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        r, c = 0, 0

        ans = ""
        for letter in target:
            val = (ord(letter)-ord('a'))
            nr, nc = val//5, val%5

            ans += (
                "L"*max(0, c-nc) 
                + "D"*max(0, nr-r)
                + "U"*max(0, r-nr)
                + "R"*max(0, nc-c)
                + "!"
            )

            r, c = nr, nc
        
        return ans
