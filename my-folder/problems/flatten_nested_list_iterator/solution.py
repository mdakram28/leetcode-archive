# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from pprint import pprint
class NestedIterator:
    # def parse(self, item):
    #     if item.isInteger():
    #         return item.getInteger()
    #     return list(map(self.parse, item.getList()))
        
    def __init__(self, nestedList: [NestedInteger]):
        self.l = nestedList
        self.idx = 0

        while self.idx < len(self.l) and not self.l[self.idx].isInteger():
            self.it = NestedIterator(self.l[self.idx].getList())
            if self.it.hasNext():
                break
            self.idx += 1
        else:
            self.it = None

    def next(self) -> int:
        if self.it is None:
            ret = self.l[self.idx].getInteger()
        else:
            ret = self.it.next()
            if self.it.hasNext():
                return ret

        self.idx += 1
        while self.idx < len(self.l) and not self.l[self.idx].isInteger():
            self.it = NestedIterator(self.l[self.idx].getList())
            if self.it.hasNext():
                break
            self.idx += 1
        else:
            self.it = None
            
        return ret

    
    def hasNext(self) -> bool:
        return self.idx < len(self.l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())