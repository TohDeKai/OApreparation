# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        can have only 3 moves

        means we can replace top 3 biggest
        OR
        top 2 biggest + smallest
        OR
        biggest + top 2 smallest
        OR
        top 3 smallest

        we can sort the array and compare minimum difference for the respective cases
        """
        nums = sorted(nums)
        if len(nums) <= 3:
            return 0
        res = nums[-4] - nums[0]  # replacing top 3 biggest
        res = min(res, nums[-3] - nums[1])  # top 2 biggest + smallest
        res = min(res, nums[-2] - nums[2])  # biggest + top 2 smallest
        res = min(res, nums[-1] - nums[3])  # replacing top 3 smallest
        return res
