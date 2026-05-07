class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        result = []
        n = len(s)
        cycle_len = 2 * numRows - 2
        
        for i in range(numRows):
            for j in range(0, n - i, cycle_len):
                # Primary character in the vertical column
                result.append(s[j + i])
                
                # Diagonal character (omitted for the first and last rows)
                if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                    result.append(s[j + cycle_len - i])
                    
        return "".join(result)
