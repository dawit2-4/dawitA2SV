class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(left, right, s):
            if left > right:
                return
            res = s[left]
            s[left] = s[right]
            s[right] = res
            left += 1
            right -= 1
            rev(left, right, s)
        return rev(0, len(s) - 1, s)
            
        
