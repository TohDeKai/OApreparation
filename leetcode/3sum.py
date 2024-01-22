# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force Approach
        Iterate for every element i
            Iterate for every element j
                Iterate for every element k
                    if k == -(i + j) and k != i != j:
                        add i,j,k to res
        O(n^3)

        Optimised Solution
        Sort the array -> O(nlogn)
        Iterating by 3s:
            have l and r pointer
            if l + r == -i:
                append [l,r,i]
                extend l and r if it is same as the next number to avoid duplicate
            elif l + r < -i:
                l += 1 so it becomes more positive
            else:
                r += 1 so it becomes more negative
        return res
        O(n^2)
        """

        nums = sorted(nums)

        pointer, n = 0, len(nums)

        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
