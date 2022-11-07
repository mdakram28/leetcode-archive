class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in ret:
                ret[k] = []
            ret[k].append(s)
        return list(ret.values())