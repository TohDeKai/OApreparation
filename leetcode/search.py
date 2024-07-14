# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        If L is smaller than center, means before pivot
            if target is bigger than L and smaller than center, means its in btwn
            else if target is bigger than L and center, means its to the right
            if target is smaller than L and center, means to the right
            if target is smalelr than L but bigger than center - not possible
        4 5 6 7 0 1 2
        ELSE if L is bigger than center, means after pivot
            if target is smaller than L but bigger than center, means to the right
            else if target is bigger than L and center, means in between
            if target is smaller than L and smaller than center, means in between
            if target is bigger than L and smaller than center - not possible
            if target is bigger than L and center. in between
        6 7 0 1 2 3 4 5
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            center = (l + r) // 2
            if target == nums[center]:
                return center

            # Left side is sorted
            if nums[l] <= nums[center]:
                if nums[l] <= target < nums[center]:
                    r = center - 1
                else:
                    l = center + 1
            # Right side is sorted
            else:
                if nums[center] < target <= nums[r]:
                    l = center + 1
                else:
                    r = center - 1

        return -1
