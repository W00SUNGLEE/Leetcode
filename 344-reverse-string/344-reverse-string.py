class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s)-1
        
        while head < tail:
            tmp = s[tail]
            s[tail] = s[head]
            s[head] = tmp
            
            head += 1
            tail -= 1