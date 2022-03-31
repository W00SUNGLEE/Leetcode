# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        head = 1
        tail = n
        node = 0
        
        while head != tail:
            node = (head+tail)//2
            
            if isBadVersion(node):
                tail = node
            else:
                head = node + 1
        return head     