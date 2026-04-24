class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
            
        n, m = len(haystack), len(needle)
        
        # Only need to loop up to where the needle could still fit
        for i in range(n - m + 1):
            # Check if the substring matches the needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1
