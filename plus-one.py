class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Convert list of digits to an integer string, add 1, then map back to list
        num = int("".join(map(str, digits))) + 1
        return [int(char) for char in str(num)]
