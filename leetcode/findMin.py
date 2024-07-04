# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Brute force solution O(n) -> just have to iterate through every element and find smallest

        Since the original array is sorted, but just rotated, we can take the concept of binary search

        take the head and end. whichever is smaller, half it and move the other pointer. and check again

        3 4 5 6 1 2
        """

        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            center = (l + r) // 2
            res = min(res, nums[center])
            if nums[center] > nums[r]:
                l = center + 1
            else:
                r = center - 1

        return res
