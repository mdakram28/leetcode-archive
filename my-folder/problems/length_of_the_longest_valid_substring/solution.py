def make_trie(words):
    root = {}
    for word in words:
        node = root
        for c in word:
            node = node.setdefault(c, {})
        if '$' not in node:
            node['$'] = 1
    return root

def find_min_end(root, word, offset):
    node = root
    for i in range(offset, len(word)):
        if word[i] not in node: return float('inf')
        node = node[word[i]]
        if '$' in node:
            return i
    return float('inf')

from sortedcontainers import SortedList

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        root = make_trie(forbidden)
        
        ends = [find_min_end(root, word, i) for i in range(len(word))]
        curr_end = SortedList()
        # print(ends)
        
        l = 0
        ans = 0
        for r in range(len(word)):
            curr_end.add(ends[r])
            while len(curr_end) > 0 and curr_end[0] <= r:
                # print("Removing", ends[l], "from", curr_end)
                curr_end.remove(ends[l])
                l += 1
            # print(l ,r, curr_end)
            ans = max(ans, r-l+1)
        return ans
    
    
    
    