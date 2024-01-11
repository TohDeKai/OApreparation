# problem link: https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Brute-force:
        For every element in the list, go through the rest of the list to find a duplicate.
        If duplicate, return true. Else, if able to iterate through to last element, return false.
        O(n^2) time

        Optimised:
        Create a hashmap to keep count of the number of times an element has appeared
        Iterate through the list. If element not already in hashmap, add it. If already in hashmap, return true.
        If iterate to last element, return false.
        O(n) time but need O(n) space complexity too
        """

        # creating hashmap to keep count
        count = {}

        # iterating through list
        pointer, n = 0, len(nums)
        while pointer < n:
            if nums[pointer] not in count:
                count[nums[pointer]] = 1
                pointer += 1
            else:
                return True

        # If it reaches this point, it means pointer = n, which means iterated through the whole list
        return False
