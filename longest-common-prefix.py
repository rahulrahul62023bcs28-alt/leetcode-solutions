class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Sort the array lexicographically
        strs.sort()
        
        # Compare characters between the first and last string only
        first = strs[0]
        last = strs[-1]
        result = []
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])
            
        return "".join(result)
