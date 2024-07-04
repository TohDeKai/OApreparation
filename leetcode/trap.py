# https://leetcode.com/problems/trapping-rain-water/description/


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        at each col, water can only be of a height of its maximum point on its left or right, whichever is lower
        1. have a left pointer and right pointer
        2. it will keep track of maxLeft and maxRight
        3. move pointer at whichever height is smaller and update
        4. vol of water collected at each updated point will be the smaller of maxLeft or maxRight minus its current height
        5. continue until the pointers meet
        """
        l, r = 0, len(height) - 1
        maxLeft = maxRight = 0
        res = 0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] < height[r]:
                l += 1
                res += max(0, min(maxLeft, maxRight) - height[l])
            else:
                r -= 1
                res += max(0, min(maxLeft, maxRight) - height[r])

        return res
