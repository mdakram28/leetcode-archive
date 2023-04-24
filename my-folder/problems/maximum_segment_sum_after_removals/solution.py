from sortedcontainers import SortedList

class Node:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        
    def insert(self, node):
        if self.val > node.val:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
    
    def min_val(self):
        node = self
        val = None
        while node:
            val = node.val
            node = node.left
        return val
    
    def max_val(self):
        node = self
        val = None
        while node:
            val = node.val
            node = node.right
        return val
    
    def successor(self):
        node = self
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        return None
    
    def predecessor(self):
        node = self
        while node.parent:
            if node.parent.right == node:
                return node.parent
            node = node.parent
        return None
    
    def print(self, pref='', sign=""):
        print(f"{pref}━({self.val})")
        if self.left:
            self.left.print(pref+" ┃")
        else:
            print(f"{pref} ┃━()")
        if self.right:
            self.right.print(pref+" ┃")
        else:
            print(f"{pref} ┃━()")
    
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        sums = []
        ans = []
        freq = defaultdict(int)
        
        # root = Node(-1)
        # root.insert(Node(n))
        sl = SortedList([-1, n])
        
        
        total = 0
        for i in range(n):
            total += nums[i]
            nums[i] = total
        
        nums.append(0)
        
        sums.append(-total)
        freq[total] += 1
        
        for rem in removeQueries:
            # print(sums)
            
            # node = Node(rem)
            # root.insert(node)
            sl.add(rem)
            i = sl.index(rem)
            prev_i = sl[i-1]
            next_i = sl[i+1]
            
            # root.print()
            # print(prev_i, next_i)
            
            prev_sum = nums[next_i-1] - nums[prev_i]
            freq[prev_sum] -= 1
            
            curr_sum = nums[rem-1] - nums[prev_i]
            heappush(sums, -curr_sum)
            freq[curr_sum] += 1
            
            curr_sum = nums[next_i-1] - nums[rem]
            heappush(sums, -curr_sum)
            freq[curr_sum] += 1
            
            # print(freq)
            while sums and freq[-sums[0]] == 0:
                # print(f"{-sums[0]} has been removed")
                heappop(sums)
            ans.append(-sums[0] if sums else 0)
        
        return ans
            
        
        
        
        