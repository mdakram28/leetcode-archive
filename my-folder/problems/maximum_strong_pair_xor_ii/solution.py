
    
        
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        max_num = nums[-1]
        max_bit = len(bin(max_num)) - 1
        
        root = {}
        
        def trie_add(num):
            node = root
            for i in range(max_bit, -1, -1):
                bit = (num >> i) & 1
                par = node
                node = node.setdefault(bit, {})
            if "#" in node:
                node["#"] += 1
            else:
                node["#"] = 1
        
        def trie_remove(num, i, node):
            if i == -1:
                node["#"] = node.get("#", 1) - 1
                if node["#"] == 0:
                    del node["#"]
                return
            bit = (num >> i) & 1
            child = node.setdefault(bit, {})
            trie_remove(num, i-1, child)
            if len(child) == 0:
                del node[bit]
            
        
        def trie_get_max_xor(num):
            node = root
            ret = 0
            for i in range(max_bit, -1, -1):
                bit = (num >> i) & 1
                if bit == 1:
                    if 0 in node:
                        node = node[0]
                        ret |= 0<<i
                    else:
                        node = node[1]
                        ret |= 1<<i
                else:
                    if 1 in node:
                        node = node[1]
                        ret |= 1<<i
                    else:
                        node = node[0]
                        ret |= 0<<i
            return ret
        
        ans = 0
        r = 0
        for l in range(len(nums)):
            if l > 0:
                trie_remove(nums[l-1], max_bit, root)
            while r < len(nums) and (nums[r]-nums[l]) <= nums[l]:
                trie_add(nums[r])
                r += 1
            
            b = trie_get_max_xor(nums[l])
            ans = max(ans, nums[l]^b)
            
        

        return ans