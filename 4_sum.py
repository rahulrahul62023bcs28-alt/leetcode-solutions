class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return self.kSum(nums, target, k=4, start=0)

    def kSum(self, nums: list[int], target: int, k: int, start: int) -> list[list[int]]:
        result = []
        n = len(nums)
        
        # Base case validations
        if start >= n or nums[start] * k > target or nums[-1] * k < target:
            return result
            
        # Base Case: Solve 2-Sum using the two-pointer technique
        if k == 2:
            left, right = start, n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
            return result

        # Recursive Case: Reduce K-Sum to (K-1)-Sum
        for i in range(start, n - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
                
            # Recursively solve for the remaining targets
            sub_results = self.kSum(nums, target - nums[i], k - 1, i + 1)
            for subset in sub_results:
                result.append([nums[i]] + subset)
                
        return result
