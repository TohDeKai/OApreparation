# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        for every elem, take target - numbers[i] and carry out binary search
        O(nlogn)

        2 pointer, if sum is bigger, move r leftwards, if smaller, move l rightwards
        O(n)
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l + 1, r + 1]
            elif curr < target:
                l += 1
            else:
                r -= 1
