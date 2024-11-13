# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        iterate through every element, starting from nums[1]
        if nums[pointer-1] > 0, add it to nums[pointer]
        compare against res.
        if nums[pointer-1] <= 0, means the cumulative sum is negative or 0, and hence better to restart the cumulative count, so you just leave it instead of adding it
        """
        res = nums[0]
        pointer, n = 1, len(nums)

        while pointer < n:
            if nums[pointer-1] >= 0:
                nums[pointer] += nums[pointer-1]
            pointer += 1
        return max(nums)