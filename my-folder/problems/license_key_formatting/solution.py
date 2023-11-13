class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        # print(list(pairwise(accumulate(chain((0, fg), repeat(k, ceil((len(s)-fg)/k)))))))
        return '-'.join(
            s[a:b] 
            for a, b in pairwise(accumulate(
                chain(
                    (0, len(s)%k) if len(s)%k > 0 else (0,),
                    repeat(k, len(s)//k)
                )
            ))
        ).upper()