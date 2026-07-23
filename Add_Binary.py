class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the current binary digit and calculate new carry
            result.append(str(total % 2))
            carry = total // 2
            
        # Reverse the result list and join into a string
        return "".join(result[::-1])
