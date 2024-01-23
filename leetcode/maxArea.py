# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        find maximum volume of water
        volume = height * width
        height will be the minimum of the 2 bounded sides
        width will be difference between the 2 lines

        brute force
        find every possible volume, compare
        for every element i,
            for every element j,
                volume = min(height[i],height[j]) * (j-i)
                res = max(volume,res)
        return res
        O(n^2)

        optimised
        have a left and right pointer
        move the lower height pointer
        calc volume and compare against res
        stop when l and r pointer meet
        O(n) one pass
        """

        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            res = max(vol, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res
